<?php
session_start();
include 'opendbDSP.php'; 
	$myFile=$_GET['id'];
	$typeArray=array();
	$termArray=array();
	$groupArray=array();
	$query='select * from transcription t,lectvideo n where t.videoID=n.videoID and videoName="'.$myFile.'"';
	$query2='select max(seek) as maxseek from transcription t,lectvideo n where t.videoID=n.videoID and videoName="'.$myFile.'"';
	$query3='select distinct type from singleterm t,lectvideo n where t.videoID=n.videoID and videoName="'.$myFile.'"';
	$result3=mysql_query($query3) or die(mysql_error());
	if(mysql_num_rows($result3)!=0)
	{
		While($record3=mysql_fetch_assoc($result3))
		{
			$type=$record3['type'];
			$typeArray[]=$type;
		}
		for($i=0; $i<sizeof($typeArray); $i++)
		{
			$groupArray=[];
			$count=0;
			$query4='select * from singleterm t,lectvideo n where t.videoID=n.videoID and videoName="'.$myFile.'" and type="'.$typeArray[$i].'" order by startTime';
			$result4=mysql_query($query4) or die(mysql_error());
			if(mysql_num_rows($result4)!=0)
			{
				while($record4=mysql_fetch_assoc($result4))
				{
					$start=$record4['startTime'];
					$id=$record4['termID'];
					$end=$record4['endTime'];
					$term=$record4['term'];
					$groupArray[$start."~".$id]=$term;
					$count++;
				}
				$termArray[$i]=$groupArray;
				
			}
		}
	}

	$result=mysql_query($query) or die (mysql_error());
	$result2=mysql_query($query2) or die (mysql_error());
	$bArray=array();
	$cArray=array();
	if(mysql_num_rows($result)!=0)
	{
		$record=mysql_fetch_assoc($result);
		$record2=mysql_fetch_assoc($result2);
		$videoID=$record['videoID'];
		$seek=$record2['maxseek'];
		$bArray=segment($seek,10);
		$dArray=segment($seek,50);

		

	}
	
	$cArray=array("one"=>$videoID,"two"=>$bArray,"three"=>$termArray,"four"=>$dArray);
	echo json_encode($cArray);

	
	function segment($seek,$value)
	{
		$average=$seek/$value;
		$total=$average*$value;
		$leftover=0;
		if($seek-$total>0)
		{
			$leftover=$seek-$total;
			$average++;
		}
		$seekvalue=0;
		for($i=0; $i<$average; $i++)
		{
			$bArray[]=$seekvalue;
			if($i!=$average-1) //you need for left over time
				$seekvalue=$seekvalue+$value;
			else
				$seekvalue=$seekvalue+$leftover;
				
		}
		return $bArray;
	}

?>