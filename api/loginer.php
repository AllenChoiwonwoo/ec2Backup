<?php
// error_reporting(E_ALL);
// ini_set("display_errors", 1);
  // require 'pdo_conn.php';
  try {
    $pdo = "mysql:host=13.209.50.185;port=3306;dbname=choi;charset=utf8";
    $pdo_conn = new PDO($pdo, "wonwoo", "cww1003");
    $pdo_conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    $pdo_conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $inputEmail = $_GET['inputEmail'];
    $inputPasswd = $_GET['inputPasswd'];
    // $inputEmail = "gogodnjsdn@naver.com";
    // $inputPasswd = "cww123456789";

    // error_log(date("Y-m-d H:i:s")
    // ."\n 아이디 : ".$inputEmail."   비번 : ".$inputPasswd."\n"
    // , 3, "/var/www/html/phplog.log");



    // echo $inputEmail.$inputPasswd."<br>";
        //
        $query = "SELECT id, userEmail, userName, userNickname, user_status from userinfo
        where userEmail = ? AND userPasswd = ?";
          // $stmt = $pdo_conn->prepare("INSERT INTO userinfo (userEmail, userName, userNickname, userPasswd, createddate) VALUES (?, ?, ?, ?, NOW())");
        $stmt = $pdo_conn->prepare($query);
        // echo $query;
        $stmt->bindParam(1,$inputEmail);
        $stmt->bindParam(2,$inputPasswd);

        $stmt->execute();
        // echo "2";
        $row = $stmt->fetchAll(PDO::FETCH_ASSOC);
        // echo $row.__len__();
        // echo count($row);
        // echo "3";
        // print_r($row);
        // echo "4";
        // echo $row['userName'];
        // echo $row['userNickname'];
        $json_all = json_encode($row,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
        // 2-2. 데이터가 어떤형인지, 문자인코딩이 무었인지 명시해준다.             //
        header('Content-Type: application/json; charset=utf8');                 // 이 해더가 있음으로 해서 json을 보여주기 쉬운형태로 화면에 표시된다.
        // 2-3. 데이터를 (화면에 )출력해준다.
        echo urldecode($json_all);
        // echo "<br>".count($json_all);
        // $userName = $row[0];





        // echo "string";


  } catch (PDOException $e) {
      echo $e->getMessage();
      echo "실패";

  }

  //
  // $inputEmail = $_GET['inputEmail'];
  // // $inputName = $_GET['inputN'];
  // // $inputNickname = $_GET['inputNickname'];
  // $inputPasswd = $_GET['inputPasswd'];




// header('Content-Type: application/json');
  // echo '[{"aBoolean":"true"}]'; //이거만 있어도 json은 잘 가네


// header('Content-Type: application/json');
// $member1 = array("aBoolean" => "true");
// $member2 = array("aBoolean" => ($inputEmail. $inputName. $inputNickname .$inputPasswd));
// // $member3 = array("name" => "이주노", "height" => "172cm", "weight" => "53kg");
// //
// // 3명의 정보를 memberData변수에 저장
// $memberData = array($member1, $member2);
// //
// // // 3명의 데이터가 JSON Array 문자열로 변환됨
// $output =  json_encode($memberData,JSON_UNESCAPED_UNICODE);
// //
// // // 출력
// echo  urldecode($output);
// //echo json_encode($output,JSON_UNESCAPED_UNICODE);


 ?>
