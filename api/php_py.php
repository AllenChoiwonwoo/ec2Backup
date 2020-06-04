
    <?php
    // 목적 : 데이터베이스에서 새생품데이터를 받아서
    //        json형으로 보여주는 코드이다
    //
    // 요소별 기능설명 :
    //     'pdo_conn.php' : pdo를 활용하여 mysql에 연결하게 하는 파일이다.
    //     get_time() : 코드가 진행하는데 걸린 시간을 계산하는 코드이다
    //
    // 전체 시나리오 :
    //     1. new_products 테이블에서 데이터를 불러온다.
    //     2. 데이터를 json형으로 변환한다.
    //     3. 데이터를 화면에 띄운다.
    //
    // 사용 라이브러리 :
          // pdo : 열결해주는 라이브러리
          //  (전반적 + fetch) https://idchowto.com/?p=20119   ,  https://www.ibm.com/support/knowledgecenter/ko/SSEPGG_11.1.0/com.ibm.swg.im.dbclient.php.doc/doc/t0023505.html
          // json_encode : json형으로 변환해주는 라이브러리
          //   (

    error_reporting(E_ALL);
    ini_set("display_errors", 1);

    require 'pdo_conn.php';

    function get_time() {
        list($usec, $sec) = explode(" ", microtime());
        return ((float)$usec + (float)$sec);
    }
      $start = get_time();

      // 1-1. new_products 테이블에서
      //    쇼핑몰이름, 이미지주소, 상품명, 가격, 개수 를 가져오게한다.
      $query = "SELECT mall_name, img_src, prodname, price, count FROM new_products";

      $stmt = $pdo_conn->prepare($query);                                                       //준비시킨다. 여러게의 쿼리를 prepare시킨후 한번에 execute할 수도 있다.
      $stmt->execute();
      $all = $stmt->fetchAll(PDO::FETCH_ASSOC);                                           //fetchAll(PDO::FETCH_ASSOC) 를 통해서 데이터를 '컬럼명'->'레코드' 형태의 array를 가진  array를 만들 수 있다 => json화가 용이
      // 2-1. 클라이언트가 요청값을 쉽게 받아갈 수 있도록 json 형태로 변환시킨다.
      $json_all = json_encode($all,JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
      // 2-2. 데이터가 어떤형인지, 문자인코딩이 무었인지 명시해준다.             //
      header('Content-Type: application/json; charset=utf8');
      // 2-3. 데이터를 (화면에 )출력해준다.
      echo urldecode($json_all);

      $end = get_time();
      $time = $end - $start;

      // ____ $all 을 json_encode하기 전 하나하나 배열을 만들어 json을 만드는 코드.____
      // $list_data = array();
      // while($row=$stmt->fetch(PDO::FETCH_ASSOC)){
      //     $item = array("mall_name" => $row['mall_name']
      //                   , "img_src" => $row['img_src']
      //                   , "prodname" => $row['prodname']
      //                   , "price" => $row['price']
      //                  , "count" => $row['count']
      //                  );
      //
      //     array_push($list_data, $item);
      //     }
      // echo json_encode($list_data,JSON_UNESCAPED_UNICODE);
      // ______________________________________________________________________________

  // echo "<br>".$time.'sec';
     ?>
