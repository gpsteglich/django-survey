from django import forms

from dynamicForms.models import FormEntry, FieldEntry
from dynamicForms import fields

class EntryForForm(forms.ModelForm):
	field_entry_model = FieldEntry

	class Meta:
		model = FormEntry

	def __init__(self, form, context, *args, **kwargs):
		"""
		Dynamically add each of the form fields for the given form model
		instance and its related field model instances.
		"""
		self.form = form
		self.form_fields = form.fields.visible()
		# Create the form fields.
		for field in self.form_fields:
			field_key = field.slug
			field_class = fields.CLASSES[field.field_type]
			field_args = {"question": field.label, "required": field.required,
							"help_text": field.help_text}
			arg_names = field_class.__init__.__code__.co_varnames
			if "choices" in arg_names:
				choices = list(field.get_choices())
				if (field.field_type == fields.SELECT and
						field.default not in [c[0] for c in choices]):
					choices.insert(0, ("", field.placeholder_text))
				field_args["choices"] = choices
			initial_val = None
			try:
				initial_val = field_entries[field.id]
			except KeyError:
				try:
					initial_val = initial[field_key]
				except KeyError:
					initial_val = Template(field.default).render(context)
			if initial_val:
				if field.is_a(*fields.MULTIPLE):
					initial_val = [x.strip() for x in initial_val.split(",") if x.strip()]
				if field.field_type == fields.CHECKBOX:
					initial_val = initial_val != "False"
				self.initial[field_key] = initial_val
			self.fields[field_key] = field_class(**field_args)
	def save(self, **kwargs):
		"""
		Get/create a FormEntry instance and assign submitted values to
		related FieldEntry instances for each form field.
		"""
		entry = super(FormForForm, self).save(commit=False)
		entry.form = self.form
		entry.entry_time = now()
		entry.save()
		entry_fields = entry.fields.values_list("field_id", flat=True)
		new_entry_fields = []
		for field in self.form_fields:
			field_key = field.slug
			value = self.cleaned_data[field_key]
			if isinstance(value, list):
				value = ", ".join([v.strip() for v in value])
			if field.id in entry_fields:
				field_entry = entry.fields.get(field_id=field.id)
				field_entry.value = value
				field_entry.save()
			else:
				new = {"entry": entry, "field_id": field.id, "value": value}
				new_entry_fields.append(self.field_entry_model(**new))
		if new_entry_fields:
			self.field_entry_model.objects.bulk_create(new_entry_fields)
		return entry
