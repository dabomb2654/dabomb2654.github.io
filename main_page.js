console.log("HEY! I WORK!");
$(document).ready(function(){
	var url = "https://github.com/dabomb2654/dabomb2654.github.io/blob/master/zuka_performances-performances2000.csv"; 
	$.get(url, function(data){
		console.log(data)
	});
});
