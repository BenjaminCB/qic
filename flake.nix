{
    description = "Flake utils demo";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
        flake-utils.url = "github:numtide/flake-utils";
        npm-builder.url = "github:BenjaminCB/npm-builder";
    };

    outputs = { self, nixpkgs, flake-utils, npm-builder }:
        flake-utils.lib.eachDefaultSystem (system:
            let
                pkgs = nixpkgs.legacyPackages.${system};
            in {
                devShells.default = pkgs.mkShell {
                    nativeBuildInputs = with pkgs; [
                        python39
                        python39Packages.pip
                        python39Packages.virtualenv
                    ];

                    shellHook = ''
                    '';
                };
            }
        );
}
