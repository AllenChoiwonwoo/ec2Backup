<?php
error_reporting(E_ALL);

ini_set("display_errors", 1);



// echo "gfdgfdgdgd";



// exec("python php_python.py", $out, $status);
//
// echo $out[0];
// echo $out[1];

$result = shell_exec("python3 php_python.py");
// $var = "\uac00\ub098\ub2e4";
// $result = passthru("python3 php_python.py");
echo $result."<br>";
$edited64 = substr($result, 2, -1);
// substr($str, int1(앞에서 몇번째부터) ,int2(뒤에서 몇번째까지) )
// 문자열을 하나의 배열로 보고, 앞에서 int1 번째부터, 뒤에서 int2번째 문자까지만 가져와 하는 코드


// $conv = $result
echo "<br>";
// $edited_result = str_replace('b','',$result);
// $edited_result = str_replace("'","",$edited_result);
// echo $edited_result."<br>";
echo gettype($result);
echo "<br><br>";
// $var2 = "\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4";
// print_r($var2);
echo "<br>";

// $var = "b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'";
          //@@ https://php.net/manual/en/function.unpack.php
        // b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'
        // $binarydata = "\x04\x00\xa0\x00";
        // $array = unpack("cchars/nint", $var);
        // print_r($array);
// print_r($var);
// echo $var." 여기까지가 변환되는 바이트어레이<br>";
// echo gettype($var)."<br>";
echo "와;;;;;"."<br>";


// $a = " \n";
  $a = $result;
  // $b = "123 sdf";
  $b = $var;

  echo ctype_space($a);
  if(ctype_space($a) == NULL) echo "a = null";
  echo strlen($a)."개";   # bytearray의 길이를 반환
  echo mb_strlen($a, 'utf8')."개";   #변환된 문자(utf8)의 개수 반환(눈에 보이는 대로)
  // 1
  echo "<br>";
  echo ctype_space($b);
  if(ctype_space($b) == NULL) echo "b = null";
  echo strlen($b)."개";
  echo mb_strlen($b,'utf8')."개";
  // b = null





// echo $var;
// echo unicode_encode($var).PHP_EOL;

if (!function_exists('unicode_encode')) {
    function unicode_encode($str) {
        return substr(json_encode($str), 1, -1);
    }
}

if (!function_exists('unicode_decode')) {
    function unicode_decode($str) {
        return json_decode(sprintf('"%s"', $str));
    }
}

$in = "u'\uc138\uc158\uc774'";
//$in = '세션이';
// echo "ㅁ1 = ".unicode_encode($in).PHP_EOL."<br />\n";
// echo "ㅁ2 = ".unicode_decode($result).PHP_EOL."<br />\n";

// function guidToBytes($guid) {
//     $guid_byte_order = [3, 2, 1, 0, 5, 4, 7, 6, 8, 9, 10, 11, 12, 13, 14, 15];
//     $guid = preg_replace("/[^a-zA-Z0-9]+/", "", $guid);
//     $result = [];
//     foreach ($guid_byte_order as $offset) {
//         $result[] = hexdec(substr($guid, 2 * $offset, 2));
//     }
//     return $result;
// }
// printf(guidToBytes($var));

// printf($result)
echo iconv("cp949","UTF-8", $edited64);
echo "<br> 뭐지..? ";
// // $var4 = utf8_decode("b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4' ");
$aaaa = base64_encode('가나다');
echo $aaaa;
// echo base64_ecode(
//
// // echo $result;
// // $string = mb_convert_encoding($result,'HTML-ENTITIES','utf-8');
// // echo "<br>".$string
//

// echo "<br>";
$str = base64_decode($edited64);
echo "<br>@@".$str;

echo "<br><br>";
// $valuse = (string)utf8_decode('가나다');
// // echo $valuse;// echo "<br>. iconv :";
// echo iconv("UTF-8","CP1252",'가나다');
// $exIconv = iconv.encode("가나다","UTF-8");
// $euc = '한글';
// // $e = iconv("UTF-8","EUC-KR", $euc);
// $e = iconv("UTF-8","EUC-KR", $euc);
// echo $e; #�ѱ�
?>
