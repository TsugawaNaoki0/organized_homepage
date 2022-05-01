<?php

// $str = 'export LANG=ja_JP.UTF-8; python3 weather.py https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=';
// $str = 'export LANG=ja_JP.UTF-8; python3 weather.py ';

  // echo shell_exec("$str".$_POST["confirm0"]);
  // echo shell_exec("$str".$_POST["confirm0"]);
  // echo shell_exec("$str");

  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 wea_generator.py");



  echo shell_exec("export LANG=ja_JP.UTF-8; python3 weather.py");




  // // 気象庁のAPIにて気象情報取得
  // $url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json";
  //
  // $weather_json = file_get_contents($url);
  // $weather_array = json_decode($weather_json, true);
  //
  // $date = $weather_array["0"]["timeSeries"]["0"]["timeDefines"]["0"];
  // $jma_weather = $weather_array["0"]["timeSeries"]["0"]["areas"]["0"]["weathers"]["0"];
  // $jma_rainfall = $weather_array["Feature"]["0"]["Property"]["WeatherList"]["Weather"]["0"]["Rainfall"];
  //
  // echo "日時:" . $date . "\n";
  // echo "今日の天気:" . $jma_weather. "\n";
  // echo "雨量:" . $jma_rainfall. "\n";
  //







  ?>
