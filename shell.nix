with import <nixpkgs> {};

( let
    wordcloud = pkgs.python3Packages.buildPythonPackage rec {
      pname = "wordcloud";
      version = "1.7.0";

      src = pkgs.python3Packages.fetchPypi{
        inherit version; inherit pname;
        sha256 = "1cpg9ypd9ak1b516i40hd1hdll5hhhkjjpf06mp9x1ha6n8bklms";
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
