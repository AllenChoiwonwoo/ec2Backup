<?php echo "예멍 예멍 예멍이~";

    function get_time() {//시간측정 함수
        list($usec, $sec) = explode(" ", microtime());
        return ((float)$usec + (float)$sec);
    }
    echo "<br>".get_time();
?>
