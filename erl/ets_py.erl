-module(ets_py).
-export([run/0]).

run() ->
  io:fwrite("Starting!~n"),
  Input = io:get_line(""),
  io:fwrite("~p~n",[Input]).