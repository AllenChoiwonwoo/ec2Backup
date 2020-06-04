<?php
  $gotOrderData = $_POST['orderData'];
  $arr = json_decode($gotOrderData,true);

  // https://zetawiki.com/wiki/PHP_json_decode()
  // 이거없었으면 큰일날뻔 역시 꼼꼼히 봐야해
  // $str = $arr["buyer_name"];
  //
  //
  // """
  // 서버에서 주문내역을 받는다.
  // 주문내역대로 각 쇼핑몰에 주문을 넣고, 쇼핑몰의 주문번호와 입금계좌를 받아온다
  //   쇼핑몰의 주문번호에 접근할 수 있는 내 주문번호를 생성한다.
  //     (클라이언트에서 서버에 내 주문번호를 보내서 주문내역을 확일할 수 있어야하겠다.)
  // 주문내역과 주문번호, 입금계좌를 서버에 저장한다.
  // 클라이언트에 응답을 보내고 . 주문번호와 입금할 계좌를 알려준다.
  //
  // """

  // $gotOrderData = '{"selectedItems":
  //   [
  //     {"mallName":"vintagetalk","img_src":"https:\/\/vintagetalk.co.kr\/web\/product\/medium\/H46214.jpg","prodName":"USA 울 풀집업 스웨터 여자S","prodNumb":"H46214","price":"1,600원 (95% 할인)","prodHref":"https:\/\/vintagetalk.co.kr\/product\/detail.html?product_no=583575&cate_no=1&display_group=2"}
  //     ,{"mallName":"vintagetalk","img_src":"https:\/\/vintagetalk.co.kr\/web\/product\/medium\/H46436.jpg","prodName":"USA 폴리 패딩 자켓 키즈2T","prodNumb":"H46436","price":"1,600원 (95% 할인)","prodHref":"https:\/\/vintagetalk.co.kr\/product\/detail.html?product_no=583797&cate_no=1&display_group=2"}
  //   ],
  //   "buyer_name":"최원우"}';
  // $arr = json_decode($str,true);

  // echo $arr["selectedItems"][1]["prodName"]."<br>";
  // echo count($arr["selectedItems"])."<br>";
  // echo $arr["buyer_name"]."<br>";

  echo date("YmdH-is").",".date("Y-m-d");
  //데이터는 주문번호, 주문날짜 순이다.
  //@ 주문상태와 운송장 번호도 서버에서 가져와야한는데. 서버 db에 저장된 값을 사용자가 요청시 가져가는시으로 해야한다.
  //@ 입금기한(payday)E도 서버에서 계산해서 주느게 편할 것이다. 왜냐면 안드로이드로 가면 string 이 되니까, 또한 서버에도 저장해야하고


  // while ($a <= 10) {
  //   // code...
  // }

  // error_log(date("Y-m-d H:i:s")
  // ."\n".$gotOrderData."\n".$arr["buyer_name"]."\n"
  // , 3, "/var/www/html/phplog.log");


 ?>
