<?php

/*
목적 : 앱에서 관리자가 회원정보 리스트를 요청시 보내주기 위한 프로그램이다.
    앱에서 온 조건에 맞게 검색해 앱에 보내준다.
    (전체, 전체검색, 이름검색, 아이디검색, 닉네임검색 )
*/
// error_reporting(E_ALL);
// ini_set("display_errors", 1);

require "pdo_conn.php";

$keyword = $_POST['keyword'];// 검색어
$filter = $_POST['filter']; // 구분자

// $keyword = $_GET['keyword'];// 검색어
// $filter = $_GET['filter']; // 구분자
// echo $keyword."<br>";
// echo $filter."<br>";
$keyword = "%".$keyword."%";



// 키워드와 필터값을 통해서 검색한 값을 줘야한다.
// 키워드와 필터를 적용안한값을 줘야한다.

// 관리자가 회원정보를 조회할때 어떤 조건(filter)를 걸어 검색했는지를 구분하기 위한 조건문이다.
if(empty($filter)){ //초기값(전체회원)
  // echo "전체";
  $query = "SELECT id, userEmail, userName, userNickname FROM userinfo";
  $stmt = $pdo_conn->prepare($query);
  $stmt->execute();

}elseif ($filter == 0) {// 전체조건으로 검색시
  // echo "전체검색";
  $query = "SELECT id, userEmail, userName, userNickname FROM userinfo WHERE userEmail like ? OR userName like ? OR userNickname like ? ";
  $stmt = $pdo_conn->prepare($query);
  $stmt->bindParam(1,$keyword);
  $stmt->bindParam(2,$keyword);
  $stmt->bindParam(3,$keyword);
  $stmt->execute();
  // code...
}elseif ($filter == 1) { //이메일 조건으로 검색시
  // echo "메일검색";
  $query = "SELECT id, userEmail, userName, userNickname FROM userinfo WHERE userEmail like ?";
  $stmt = $pdo_conn->prepare($query);
  $stmt->bindParam(1,$keyword);
  $stmt->execute();
  // code...
}elseif ($filter == 2) {// 이름 조건으로 검색시
  // echo "이름검색";
  $query = "SELECT id, userEmail, userName, userNickname FROM userinfo WHERE userName like ?";
  $stmt = $pdo_conn->prepare($query);
  $stmt->bindParam(1,$keyword);
  $stmt->execute();
  // code...
}elseif ($filter == 3) { // 닉네임 조건으로 검색시
  // echo "닉네임검색";
  $query = "SELECT id, userEmail, userName, userNickname FROM userinfo WHERE userNickname like ?";
  $stmt = $pdo_conn->prepare($query);
  $stmt->bindParam(1,$keyword);
  $stmt->execute();
  // code...
}

  $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
  $json_all = json_encode($all,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
  header('Content-Type: application/json; charset=utf8');
  echo urldecode($json_all);

// $query = "SELECT id, userEmail, userName, userNickname FROM userinfo";

  // error_log(date("Y-m-d H:i:s")
  // ."\n".$json_all."\n"
  // , 3, "/var/www/html/phplog.log");


 ?>
