

<!DOCTYPE html>
<html lang="ja">
 <head>
   <meta charset="utf-8">
   <link rel="stylesheet" href="./../../home.css">
   <title>HallowinGhost</title>
    <link rel="icon" href="ghost.png"><!-- タイトルにアイコンを設定 -->
    <link rel="apple-touch-icon" href="icon.png"><!-- iphone のアイコンを設定 -->
 </head>
 <body>
    <div class="main">
            <br>
            <h1>リボ払い</h1>
            <br>
            ※ 1ヶ月を30日(1年を360日)として計算しています
            <br>
            <form action="./code/generator.php" method="post">
              <!-- <input type="textarea" name="confirm" value=""> -->
              <label for="confirm1"><h3>借入額</h3></label><br>
              <select name="confirm0" class="form">
                  <!-- <option value="blue">青</option> -->
                  <option value="0.10">10%</option>
                  <option value="0.11">11%</option>
                  <option value="0.12">12%</option>
                  <option value="0.13">13%</option>
                  <option value="0.14">14%</option>
                  <option value="0.15">15%</option>
                  <option value="0.16">16%</option>
                  <option value="0.17">17%</option>
                  <option value="0.18">18%</option>
                  <option value="0.19">19%</option>
                  <option value="0.20">20%</option>
                  <option value="0.331">トイチ</option>
                  <option value="0.2197">トサン</option>
                  <option value="0.3375">トゴ</option>
              </select>

              <label for="confirm1"><h3>借入額</h3></label><br>
              <select name="confirm1" class="form">
                  <!-- <option value="blue">青</option> -->
                  <option value="10000000">10,000,000</option>
                  <option value="20000000">20,000,000</option>
                  <option value="30000000">30,000,000</option>
                  <option value="40000000">40,000,000</option>
                  <option value="50000000">50,000,000</option>
                  <option value="60000000">60,000,000</option>
                  <option value="70000000">70,000,000</option>
                  <option value="80000000">80,000,000</option>
                  <option value="90000000">90,000,000</option>
                  <option value="100000000">100,000,000</option>
              </select>


              <label for="confirm2"><h3>月返済額</h3></label><br>
              <select name="confirm2" class="form">
                  <!-- <option value="blue">青</option> -->
                  <option value="100000">100,000</option>
                  <option value="200000">200,000</option>
                  <option value="300000">300,000</option>
                  <option value="400000">400,000</option>
                  <option value="500000">500,000</option>
                  <option value="600000">600,000</option>
                  <option value="700000">700,000</option>
                  <option value="800000">800,000</option>
                  <option value="900000">900,000</option>
                  <option value="1000000">1,000,000</option>
              </select>
              <input type="submit" value="-----" class="form">
            </form>

            <br>
            <br>



    </div>

 </body>
</html>
