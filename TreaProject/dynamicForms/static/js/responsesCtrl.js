(function () {
	
    var app = angular.module('dynamicFormsFramework', []);
    
    /*
     * This controller handles the logic to create, edit and save a form.
     */    
    app.controller('ResponsesCtrl', function ($scope, $http, $location, $window) {

    	var responses = this;
    	responses.formId = ($location.search()).form;
        responses.versionNumber = ($location.search()).ver;
        responses.json = "";

        responses.getResponses = function(){
            $http.get(responses.formId+'/'+ responses.versionNumber+'/')
            .success(function(data){
                responses.json = data;
              /*  for(var i =0;i<responses.json.length;i++)
                    if(JSON.parse(responses.json[i]).field_type=="FileField")
                        console.log("ESTOY");
                    else console.log("NOP");*/
            })
            .error(function(data, status, headers, config){
                alert(data + status);
            })
        }

        //calls the function getResponses
        responses.getResponses();
        
        responses.isFile = function(field){
            
            var re = new RegExp("FileField");
            var res = ""
            var res = re.exec(field);
           // console.log(res);
            return res!=null;
            
        }
        
        responses.download = function(field){
        
            
            var infoFile =  /.*,(\d*),(\d*)/g.exec(field);
            var field_id = infoFile[1];
            var entry = infoFile[2];
            console.log(field_id +" "+entry);
             $http.get('download/'+field_id+'/'+ entry+'/')
            .success(function(data){
                responses.json = data;
                  responses.downloadFile(data);
                  console.log("OK");
            })
            .error(function(data, status, headers, config){
                alert(data + status);
            })
             
             
             
            
        }
        
        
        responses.str2ab = function str2ab(str) {
              var buf = new ArrayBuffer(str.length*2); // 2 bytes for each char
              var bufView = new Uint16Array(buf);
              for (var i=0, strLen=str.length; i<strLen; i++) {
                bufView[i] = str.charCodeAt(i);
              }
              return buf;
            }    
            responses.downloadFile = function(data){
                
               // var reader = new FileReader();
                var oMyBlob = new Blob([responses.str2ab(data.file)], {type : "application/zip"});
              
                saveAs(oMyBlob,"data.pdf");
                
            
            }
    });
})();
