<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="./taihou_style.css">
  </head>
  <body>
    <div class="total_main">
      <br>
      <br>
      <h1>泰鵬大学</h1>
      <br>
      <br>
      <br>
      <br>
      HOME
      <hr>
      <div class="main_left">
        <form class="" action="#" method="post">
          <div class="">
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <input type="text" name="text" value="" class="kensaku">
            <input type="submit" name="" value="検索" class="kensaku">
          </div>
        </form>
        <br>
        <br>
        ※　検索ワードは１つだけ
        <br>
        <br>
        <br>
        <?php
          $sakana =  $_POST[text];
          echo "検索ワード：「".$sakana."」";
          ?>
          <br>
          <br>
          <hr>
          <br>
          <?php
          $momoniku = file(__DIR__ . '/links.txt');
          $ebi = file(__DIR__ . '/urls.txt');

          $yaki_doufu = count($momoniku, COUNT_RECURSIVE);
          $momen_doufu = count($ebi, COUNT_RECURSIVE);

          for ($i = 0; $i < $yaki_doufu; $i++){
            if (strpos(substr($momoniku[$i], 8), $sakana) !== false){
              $index_momoniku = substr($momoniku[$i], 0, 8);
              for ($j = 0; $j < $momen_doufu; $j++){
                // echo $index_momoniku;
                if (strpos($ebi[$i], $index_momoniku) !== false){
                  // echo $index_momoniku;
                  echo "<a href=\"".substr($ebi[$i], 8)."\">".substr($momoniku[$i], 8)."</a>";
                  break;
                }
              }

              ?>
              <br>
              <br>
              <?php
              }
            }
        ?>
        <br>
        <br>
        <br>
        <br>
        <br>
      </div>
      <div class="main_right">
        <!-- <hr>
        <hr> -->
          <h1>
            <a href="./shoukai_g.php">学部紹介</a>
            <a href="#">大学の特色</a>
            <a href="#">研究や社会貢献</a>
            <a href="#">学部・大学院</a>
            <a href="#">留学・国際交流</a>
            <a href="#">留学・国際交流</a>
            <a href="#">学生生活の手引き</a>
            <a href="#">就職・キャリア</a>
          </h1>
        <hr>
          <h1>
            <a href="#">在学生の方へ</a>
            <a href="#">卒業生の方へ</a>
            <a href="#">受験生の方へ</a>
            <a href="#">保護者の方へ</a>
            <a href="#">一般・地域の方へ</a>
            <a href="#">企業・研究者の方へ</a>
          </h1>
          <div class="">
            <h2>重要</h2>
            <h3>
              <a href="#">新型コロナウイルス感染症についての大学としての対応</a>
            </h3>
          </div>
          <div class="">
            <h2>おしらせ</h2>
            <ul>
              <li>
                <a href="#">長期連休中の対応について</a>
              </li>
              <li>
                <a href="#">奨学金説明会の開催について</a>
              </li>
              <li>
                <a href="#">キャンパス内での宗教勧誘行為について</a>
              </li>
            </ul>
          </div>
          <div class="">
            <h2>大学としての取り組み</h2>
            <ul>
              <li>
                <a href="#">海岸清掃ボランティア</a>
              </li>
              <li>
                <a href="#">地域スポーツクラブとの交流大会</a>
              </li>
              <li>
                <a href="#">地元企業との共同研究</a>
              </li>
            </ul>
          </div>
        </div>
      </div>

  </body>
</html>
