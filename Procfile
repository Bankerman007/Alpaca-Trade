spec:
  name: tradebot
  services:
    web: streamlit run stream_app.py --server.port 80
  - dockerfile_path: dokku@justdev.us:tradebot
    git:
      branch: main
      deploy_on_push: true
      repo_clone_url: https://github.com/Bankerman007/Alpaca-Trade.git
    name: Alpaca-Trade