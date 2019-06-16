console.log("HEY! I WORK!");
$(document).ready(function(){
	var url = "https://github.com/dabomb2654/online-charts/blob/master/misc/zuka_performances-performances2000.csv"; 
	$.get(url, function(data){
		console.log(data)
	});
});
