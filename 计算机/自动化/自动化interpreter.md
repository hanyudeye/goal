## running open interpreter locally

interpreter --local

低性能处理器，调低参数
interpreter --local --max_tokens 1000 --context_window 3000

interpreter --model ollama/llama3 -y --context_window 3000 --max_tokens 1000 --max_output 1000

interpreter --model ollama/llama3 -y --context_window 200000 --max_tokens 8196  --max_output 8196 

## configuration

调用默认配置文件  default.yaml

interpreter --profiles

## 注意安全

You can run interpreter -y or set interpreter.auto_run = True to关闭提示，在执行危险任务时要注意随时关闭终端