<?php
// error_reporting(E_ALL);
// ini_set("display_errors", 1);
//   echo "최원우";
  require 'pdo_conn.php';
  // try {
  //   $pdo = "mysql:host=13.209.50.185;port=3306;dbname=choi;charset=utf8";
  //   $pdo_conn = new PDO($pdo, "wonwoo", "cww1003");
  //   $pdo_conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
  //   $pdo_conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  // } catch (PDOException $e) {
  //     // echo $e->getMessage();
  //     // echo "실패";
  // }
  $inputEmail = $_GET['inputEmail'];
  $inputName = $_GET['inputName'];
  $inputNickname = $_GET['inputNickname'];
  $inputPasswd = $_GET['inputPasswd'];
  // $_POST
  // $_QUErY
  // $_BODY
  // // $inputPhone = $_GET['inputPhone'];
  // // echo $inputEmail.$inputName.$inputNickname.$inputPasswd.$inputPhone;
  //
  // $query = "INSERT INTO inputinfo (inputEmail, inputName, inputNickname, inputPasswd, inputPhone, createddate) VALUES ($inputEmail, $inputName, $inputNickname, $inputPasswd, $inputPhone, NOW())";
      // $query = "INSERT INTO userinfo (userEmail, userName, userNickname, userPasswd, createddate) VALUES ($inputEmail, $inputName, $inputNickname, $inputPasswd, NOW())";
      // //

      $stmt = $pdo_conn->prepare("INSERT INTO userinfo (userEmail, userName, userNickname, userPasswd, createddate) VALUES (?, ?, ?, ?, NOW())");
      $stmt->bindParam(1,$inputEmail);
      // $st->bindParam(2, $data, PDO::PARAM_STR);
      $stmt->bindParam(2,$inputName);
      $stmt->bindParam(3,$inputNickname);
      $stmt->bindParam(4,$inputPasswd);

      // $pdo_conn->bindParm(/
      $stmt->execute();

// echo "<br>".$query."<br>";

// http://ec2-13-209-50-185.ap-northeast-2.compute.amazonaws.com/api/joiner.php?inputEmail=%22dkssudnjsdn@naver.com%22&inputName=%22choiwonwoo%22&inputNickname=%22wonwoo%22&inputPasswd=%22cww1003%22&inputPhone=%2210112341236%22

// header('Content-Type: application/json');
  // echo '[{"aBoolean":"true"}]'; //이거만 있어도 json은 잘 가네


header('Content-Type: application/json');
$member1 = array("aBoolean" => "true");
$member2 = array("aBoolean" => ($inputEmail. $inputName. $inputNickname .$inputPasswd));
// $member3 = array("name" => "이주노", "height" => "172cm", "weight" => "53kg");
//
// 3명의 정보를 memberData변수에 저장
$memberData = array($member1, $member2);
//
// // 3명의 데이터가 JSON Array 문자열로 변환됨
$output =  json_encode($memberData,JSON_UNESCAPED_UNICODE);
//
// // 출력
echo  urldecode($output);
// echo json_encode($output,JSON_UNESCAPED_UNICODE);


 ?>
