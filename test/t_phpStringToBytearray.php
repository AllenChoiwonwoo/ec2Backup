<?php

$string = "한글";

$e = iconv("UTF-8","EUC-KR", $string);
echo $e; #�ѱ�'
$u = iconv("EUC-KR","UTF-8", $e);
echo $u; #한글
echo "<br>";
echo "b'\xc7\xd1\xb1\xdb'"; #b'�ѱ�'

$result = shell_exec("python3 t_Euc-krEncode.py"); # b'\xc7\xd1\xb1\xdb'
echo $result."<br>"; #b'�ѱ�' 이 나올것이라 예상했는데 b'\xc7\xd1\xb1\xdb'이 나온다.
$edited_result = substr($result, 2, -2);
$u = iconv("EUC-KR","UTF-8", $edited_result);
echo $u;

 ?>
