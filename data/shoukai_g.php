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
      <hr>
      <div class="main_left">
        <form class="" action="./taihou.php" method="post">
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
      <div class="main_left">

    <h1>学部紹介</h1>
    <hr>
    <ul>
      <h1>法学部</h1>
      <li>
        <h2><a href="./gakubu/houritsu.html">法律学科</a></h2>
      </li>
      <li>
        <h2><a href="./gakubu/seikei.html">政治経済学科</a></h2>
      </li>

      <h1>文理学部</h1>
      <li>
        <h2><a href="./gakubu/bunkoku.html">文学専攻(国文学)</a></h2>
      </li>
      <li>
        <h2><a href="./gakubu/bunei.html">文学専攻(英文学)</a></h2>
      </li>
      <li>
        <h2><a href="./gakubu/tetsugaku.html">哲学専攻</a></h2>
      </li>
      <li>
        <h2><a href="./gakubu/shigaku.html">史学専攻</a></h2>
      </li>

      <h1>経済学部</h1>
      <li>
        <h2><a href="./gakubu/keizai.html">経済学科</a></h2>
      </li>

      <h1>商学部</h1>
      <li>
        <h2><a href="./gakubu/shou.html">商業学科</a></h2>
      </li>
    </ul>
      </div>
    </div>
  </body>
</html>
