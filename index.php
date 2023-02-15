<link rel="stylesheet" href="./home.css">
<?php

function h($s){
  return htmlspecialchars($s, ENT_QUOTES, 'utf-8');
}

session_start();
//ログイン済みの場合

  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py ".$_POST["confirm0"]." ".$_POST["confirm1"]." ".$_POST["confirm2"]);
  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 graph_maker.py ".$_POST["confirm1"]." ".$_POST["confirm2"]);
  // $fileName = basename(__FILE__);
  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 sample.py ".$fileName);
  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 sample.py index.php");
  echo shell_exec("export LANG=ja_JP.UTF-8; python3 log.py ".$_SERVER['PHP_SELF']);


  echo '';
  echo '<title>HallowinGhost</title>';
  echo '<link rel="icon" href="ghost.png"><!-- タイトルにアイコンを設定 -->';
  echo '<link rel="apple-touch-icon" href="icon.png"><!-- iphone のアイコンを設定 -->';

  echo '<div class="main">';

if (isset($_SESSION['EMAIL'])) {

  echo '<p>';
  echo '<br>';
  echo 'ようこそ' .h($_SESSION['EMAIL']) . "さん";
  echo '<br>';
  echo '<br>';
  echo '<table border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
  <td align="center">
  <img src="http://www.rays-counter.com/d507_f6_010/627cfa31a0715/" alt="アクセスカウンター" border="0" width="20">
  </td>
  </tr>
  </table>';
  echo '<br>';
  echo '<br>';
  echo '<br>';
  echo '<audio controls autoplay src="./pale_blue/02ゆめうつつ.mp3" type="audio/mp3">BGMテスト</audio>';
  echo "<h2><a href='./organized_homepage/index.php'>ホームページ</a></h2>";
  echo "<h2><a href='http://35.81.113.142/' target='_blank'>Pleasanter</a></h2>";
  echo "<h2><a href='http://35.85.44.235/glpi/index.php?noAUTO=1' target='_blank'>GLPI</a></h2>";
  echo "<h2><a href='./news.php'>ニュース</a></h2>";
  echo "<h2><a href='./idol.php'>アイドル</a></h2>";
  echo "<h2><a href='https://www.netflix.com/browse' target='_blank'>NETFLIX</a></h2>";
  echo "<h2><a href='https://saizeria-gacha.web.app/' target='_blank'>サイゼリヤN円ガチャ</a></h2>";
  echo '<br>';
  echo '<br>';
  echo "<a href=\"./riyoukiyaku.html\">利用規約</a>";
  echo '<br>';
  echo '<br>';
  echo "<h2><a href='/logout.php'>ログアウトはこちら。</a></h2>";
  echo '<br>';
  echo '<br>';



  exit;
}

  echo '</div>';
  echo '</p>';
 ?>

<!DOCTYPE html>
<html lang="ja">
 <head>
   <meta charset="utf-8">
   <link rel="stylesheet" href="./home.css">
   <title>HallowinGhost</title>
    <link rel="icon" href="ghost.png"><!-- タイトルにアイコンを設定 -->
    <link rel="apple-touch-icon" href="icon.png"><!-- iphone のアイコンを設定 -->
    <meta name="robots" content="noindex">
 </head>
 <body>

   <div id="cursor"></div>
   <div class="main">
     <div class="title_img">
       <img src="title.png" alt="" title="タイトル">
     </div>
     <a href="sms:お店の携帯番号">ショートメールで問い合わせする</a>
     <h1><font color="white">LOGIN</font></h1>

     <!--タグはここから-->


     <form  action="login.php" method="post" class="login">
       <input type="email" name="email" class="login" placeholder="E-MAIL" required>
       <br>
       <br>
       <input type="password" name="password" class="login" placeholder="PASSWORD" required>
       <br>
       <br>
       <button type="submit" class="login">_____</button>
       <br>
       <br>
       <!-- <input type="checkbox" name="q2" value="">
       <label for="q2"><a href="./riyoukiyaku.html">利用規約</a>に同意する</label> -->

       <br>
       <br>

     </form>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <!-- <form  action="qr_code.php" method="post" class="qrcode">
       <input type="email" name="email" class="qrcode" placeholder="E-MAIL" required>
       <br>
       <br>
       <br>
       <br>
       <button type="submit" class="qrcode">_____</button>
       <br>
       <br>
       <!-- <input type="checkbox" name="q2" value="">
       <label for="q2"><a href="./riyoukiyaku.html">利用規約</a>に同意する</label> -->
     <!-- </form> -->
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <br>
     <!-- <script type="text/javascript"> -->



     <!-- <h1>初めての方はこちら</h1>
     <form action="signUp.php" method="post" class="form">
       <label for="email">E-MAIL</label>
       <input type="email" name="email">
       <label for="password">PASSWORD</label>
       <input type="password" name="password">
       <button type="submit">_____</button>
       <p>※パスワードは半角英数字をそれぞれ１文字以上含んだ、８文字以上で設定してください。</p>
     </form> -->




  </div>

 </body>
</html>
