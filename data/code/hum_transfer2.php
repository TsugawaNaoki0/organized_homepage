<?php


  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 revolving.py ".$_POST["confirm0"]." ".$_POST["confirm1"]." ".$_POST["confirm2"]);
  // echo shell_exec("export LANG=ja_JP.UTF-8; python3 graph_maker.py ".$_POST["confirm1"]." ".$_POST["confirm2"]);

  echo shell_exec("export LANG=ja_JP.UTF-8; python3 human_resource2.py ".$_POST["confirm0"]);

 ?>
