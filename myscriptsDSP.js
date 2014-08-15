
//--------------------------------------------Keyword search--------------------------------------------------------------



function showResult(str){
	var mov=new XMLHttpRequest();
	mov.open("GET","searchResultsDSP.php?id="+str,true);
	mov.onreadystatechange=function(){
	if (mov.readyState==4 && mov.status==200){
		document.getElementById("fill").innerHTML=mov.responseText;}
			$(document).ready(function() {
				$(".inline").colorbox({inline:true, innerWidth:820, innerHeight:600 });
		});}
mov.send();} 


//--------------------------------------------------------------------------------------------------------------------------------------

function dynamicVideo(myFile)	
{	
	dynamic=new XMLHttpRequest();
	dynamic.open("GET","Summ.php?id="+myFile,true);
	dynamic.send();
	b=[];
	dynamic.onreadystatechange=function()
	{
		if (dynamic.readyState==4 && dynamic.status==200){
			myData=JSON.parse(dynamic.responseText);
			a=myData.one;
			b=myData.two;
			c=myData.three;
			d=myData.four;
			story='';
			var tempA=0;
			var tempB=0;

			tempTable=wholeText(c);
			document.getElementById("contain").innerHTML=tempTable;
			jwplayer().onTime(function()
			{
			var currentPosition=jwplayer().getPosition();
			var value=0;
			/*for(var k in d)
			{
				if(currentPosition>d[value] && currentPosition<d[value+1])
				{
					tempTable=wholeText(c,d[value],d[value+1]);
					document.getElementById("contain").innerHTML=tempTable;
				}
				value=value+1;
			} */
			var code=0; 
				if((currentPosition<tempA || currentPosition>tempB))
				{
					for (var x in b) 
					{
						if (currentPosition<b[b.length-1])
						{
								if (currentPosition>b[code] && currentPosition<b[code+1])
								{
								//	passString(a+"~"+b[code]+"~"+b[code]+"~"+b[code+1]);
									for (var u=0; u<c.length; u++)
									{
										for( j in c[u])
										{
											sValue=j.split("~");
											if(sValue[0] >=b[code] && sValue[0]<=b[code+1])
											{
												document.getElementById(j).innerHTML='<font color="red">'+c[u][j]+'</font>';
												document.getElementById(j).focus();
											}
											else
											{
											 document.getElementById(j).innerHTML='<font color="black">'+c[u][j]+'</font>';
											 document.getElementById(j).blur();
											}
										}
									}									
									tempA=b[code]; tempB=b[code+1]; code=0; 
									break;
								}
						}
						else
						{
							code=b.length-1;
						//	passString(a+"~"+b[code]+"~"+b[code]+"~"+b[code+1]); 
							tempA=b[code];  tempB=b[code]+10000; code=0; break;	
						}
							
						code=code+1;
					}
						
				}
			});
		}
	}	
}
function wholeText(c)
{
			tempTable='<table class="chiong" width="800" border="1"><tr>';
			//~ for(var x=0; x<c.length; x++)
			for(var x=0; x<1; x++)
			{
				story='';
				size=800/c.length;
				tempTable=tempTable+'<td valign="top"><div id="table'+c[x]+'" style="overflow-x:hidden;overflow-y:scroll;height:100px"><table width="size"><tr>';
				tempTable=tempTable+'<td>';
				for (var j in c[x])
				{				
					sValue=j.split("~");
					story=story+' <a id="'+j+'" href="#" style="color: black" onclick="jwplayer().seek('+sValue[0]+');">'+c[x][j]+'</a>';
				}
				tempTable=tempTable+story+'</td></tr></table></div></td>';
			}
			tempTable=tempTable+'</tr></table>';
			return tempTable;

}
/*function passString(id)
{

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'transcript.php?req='+id, true);
    xhr.onload = function() 
    {
		if(xhr.readyState==4 && xhr.status==200)
		{
			document.getElementById("contain").innerHTML=xhr.responseText;
		}
    }
    xhr.send(null);
} */



