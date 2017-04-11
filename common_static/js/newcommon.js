
        $(function(){ 
        //展示层 
        function showLayer(id){ 
            var layer = $('#'+id), 
                layerwrap = layer.find('.hw-layer-wrap'); 
            layer.fadeIn(); 
            //屏幕居中 
            layerwrap.css({ 
                'margin-top': -layerwrap.outerHeight()/2 
            }); 
        } 
     
        //隐藏层 
        function hideLayer(){ 
            $('.hw-overlay').fadeOut(); 
        } 
     
        $('.hwLayer-ok,.hwLayer-cancel,.hwLayer-close').on('click', function() { 
            hideLayer(); 
        }); 
     
        //触发弹出层 
        $('.show-layer').on('click',  function() {         
            var layerid = $(this).data('show-layer'); 
            showLayer(layerid); 
        }); 
     
        //点击或者触控弹出层外的半透明遮罩层，关闭弹出层 
        $('.hw-overlay').on('click',  function(event) { 
            if (event.target == this){ 
                hideLayer(); 
            } 
        }); 
     
        //按ESC键关闭弹出层 
        $(document).keyup(function(event) { 
            if (event.keyCode == 27) { 
                hideLayer(); 
            } 
        }); 
    });

        function cheack_title(){
            var title = document.getElementById('title').value;
            if (title == '' || title==undefined ||title==null|| content == ''||content==undefined||content==null) {
            document.getElementById('erroretitle').style.display = "block";
            return false;
            }
            else{
                document.getElementById('erroretitle').style.display = "none";
            }
        }
        function cheack_content(){
            var content = document.getElementById('content').value;
            if (content == ''||content==undefined||content==null) {
                document.getElementById('errorcontent').style.display = "block";
                return false;
            }
            else{
                document.getElementById('erroretitle').style.display = "none";
            }
        }
        
        $(document).ready(function() {  
      
        //Default Action  
        $("#Teasingwall").hide(); //Hide all content  
        $(".love1").addClass("active").show(); //Activate first tab  
        $("#lovewall").show(); //Show first tab content  
          
        //On Click Event  
        $(".love1").click(function() {  
            
            $("#Teasingwall").hide(); //Hide all content  
            $(".love1").addClass("active").show(); //Activate first tab  
            $("#lovewall").show(); //Show first tab content  
            return false;  
        }); 
        $(".love2").click(function() {  
            $("#lovewall").hide(); //Hide all content  
            $(".love2").addClass("active").show(); //Activate first tab  
            $("#Teasingwall").show(); //Show first tab content  
            return false;  
        }); 
      
    }); 
