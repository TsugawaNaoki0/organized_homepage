<?php

  // echo $_POST["confirm"];
  // $zandaka = $_POST["confirm1"]
  // $hensai = $_POST["confirm2"]

  echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py ".$_POST["confirm1"]." ".$_POST["confirm2"]);

  // if ($_POST["confirm"]=="10000"){
  //   echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py 10000");
  // }
  // if ($_POST["confirm"]=="20000"){
  //   echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py 20000");
  // }
  // if ($_POST["confirm"]=="40000"){
  //   echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py 40000");
  // }
  // if ($_POST["confirm"]=="100000"){
  //   echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py 100000");
  // }
  // if ($_POST["confirm"]=="200000"){
  //   echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py 200000");
  // }



 ?>
