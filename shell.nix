with import <nixpkgs> {};

( let
    wordcloud = pkgs.python3Packages.buildPythonPackage rec {
      pname = "wordcloud";
      version = "1.8.2.2";

      src = pkgs.python3Packages.fetchPypi{
        inherit version; inherit pname;
        sha256 = "Uj24h+R+hA61wuYEKCQ7sddDn9xg+JYmsXuvob5kRZw=";
      };

      propagatedBuildInputs = with pkgs.python3Packages; [
        matplotlib
        numpy
        pillow
      ];
      doCheck = false;

    };
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
      wordcloud
    ];
  }).env
