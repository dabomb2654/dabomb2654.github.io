console.log("HEY! I WORK!");
$(document).ready(function(){
	var reader = new FileReader();
	reader.onload = function (){
		document.getElementById('out').innerHTML=reader.result;
	};
	reader.readAsText('zuka_performances-performances2000.csv','utf8');
});
