
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
// 显示选中的上传的图片
    function imgPreview(fileDom){
        //判断是否支持FileReader
        if (window.FileReader) {
            var reader = new FileReader();
        } else {
            alert("您的设备不支持图片预览功能，如需该功能请升级您的设备！");
        }

        //获取文件
        var file = fileDom.files[0];
        var imageType = /^image\//;
        //是否是图片
        if (!imageType.test(file.type)) {
            alert("请选择图片！");
            return;
        }
        //读取完成
        reader.onload = function(e) {
            //获取图片dom
            var img = document.getElementById("preview");
            //图片路径设置为读取的图片
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
