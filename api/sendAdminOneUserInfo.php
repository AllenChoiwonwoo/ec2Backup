<?php
  /*
  목적 : 앱에서 관리자가 회원정보를 관리하고자 할때
          한명의 회원정보를 상세하고 보고싶어 요청하면
          이 프로그랩이 그 회원의 정보 서버db-userInfo 테이블에서 가져다 보내준다.
  파라미터값 :
          post['id']

  줄거리 :
      이메일, 이름, 닉네임, 가입일 데이터 추출방식
        사용자가 보낸 회원의id값을 받아 변수에 담는다.
        db-userInfo 테이블에서 회원id와 일치하는 데이터만 가져온다.

      총 주문개수 데이터 추출방식
        db-all_orders 테이블에서 회원id가 주문한 주문의 개수를 받아온다.

      총 주문 금액 데이터 추출방식 (  사실 주문금액은 그냥 주문을 한 금액이다.)
        db-all_orders 테이블에서 회원id가 주문한 총 금액을 받아온다.
        받아온 모든 결제금액을 더한다.

      (추후 총 결제금액을 추가해야한다. 주문을 했지만 결제를 하지 않은 주문들이 있을것이기 때문이다.)

  */
  // error_reporting(E_ALL);
  // ini_set("display_errors", 1);

  require "pdo_conn.php";

    $id = $_POST['id'];
    // $id = $_GET['id'];

    $query = "SELECT id, userEmail, userName, userNickname, createdDate, user_status FROM userinfo WHERE id = ?"; //이메일, 이름, 닉네임, 가입일 데이터 추출쿼리
    $stmt = $pdo_conn->prepare($query);
    $stmt->bindParam(1,$id);
    $stmt->execute();
    $all1 = $stmt->fetchAll(PDO::FETCH_ASSOC);
    // $json_all = json_encode($all,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
    // header('Content-Type: application/json; charset=utf8');
    // echo urldecode($json_all);
    // printf($all);
    // print_r($all1);
    // echo $all1[0]['id']."<br>";
    // echo $all1[0]['userEmail']."<br>";
    // echo $all1[0]['userName']."<br>";
    // echo $all1[0]['userNickname']."<br>";

    $query = "SELECT finalBill FROM all_orders WHERE userId = ?";
    $stmt = $pdo_conn->prepare($query);
    $stmt->bindParam(1,$id);
    $stmt->execute();
    $all = $stmt->fetchAll(PDO::FETCH_ASSOC);
    // print_r($all);
    // echo "<br>";
    // echo count($all);
    //
    $totalNumberOfOrder = count($all);

    // error_log(date("Y-m-d H:i:s")
    // ."\n".$totalNumberOfOrder."\n"
    // , 3, "/var/www/html/phplog.log");

    $totalOrderPayment = 0;
    for ($i=0; $i < $totalNumberOfOrder; $i++) {
      // echo $i;
      // print_r($all[$i]['finalBill']);
      // echo "<br>";
      $totalOrderPayment = $totalOrderPayment + $all[$i]['finalBill'];
    //   // code...
    }
    // print $totalOrderPayment;

    $all1[0]['totalNumberOfOrders'] = $totalNumberOfOrder;
    $all1[0]['totalOrderAmount'] = $totalOrderPayment;

    $json_all = json_encode($all1,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
    header('Content-Type: application/json; charset=utf8');
    echo urldecode($json_all);


 ?>
