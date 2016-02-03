var i = 1; 
var j= -1;
var list = [];
var a=list[0];
var len = list.length;
var num = 0;

function txt(){
	var strs = a.slice(0,i);

	$("#textdisp").html(strs +'|');

	if(i >= 0)
	{
		if (i != a.length)
			{
				i++;
			}
		else
			{	
				i = -1;}
	}
	

	
		
}



setInterval(txt,190);
