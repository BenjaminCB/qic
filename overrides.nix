final: prev: let
  addNativeBuildInputs = drvName: inputs: {
    "${drvName}" = prev.${drvName}.overridePythonAttrs (
      old: {
        nativeBuildInputs = (old.nativeBuildInputs or []) ++ inputs;
      }
    );
  };
in
  {} // addNativeBuildInputs "pathspec" [final.flit-core]
     // addNativeBuildInputs "pygments" [final.hatchling]
     // addNativeBuildInputs "pyzmq" [final.scikit-build-core]
     // addNativeBuildInputs "scikit-build-core" [final.distlib]
