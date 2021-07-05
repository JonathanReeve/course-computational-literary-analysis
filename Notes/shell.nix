with import <nixpkgs> {};

( let
in pkgs.python3.buildEnv.override rec {
    extraLibs = with pkgs.python3Packages; [
	    matplotlib
      spacy
      pandas
      spacy_models.en_core_web_lg
      jupyter
      jupyterlab # Dev
      scikitlearn
      nltk
      # altair
      networkx
    ];
  }).env
