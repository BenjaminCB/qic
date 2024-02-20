{
    description = "Flake utils demo";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, nixpkgs, flake-utils }:
        flake-utils.lib.eachDefaultSystem (system:
            let
                pkgs = nixpkgs.legacyPackages.${system};
                python-pkgs = pkgs: with pkgs; [
                    qiskit
                ];
            in {
                packages = rec {
                    default = pkgs.hello;
                };
                devShells.default = pkgs.mkShell {
                    nativeBuildInputs = [
                        (pkgs.python3.withPackages python-pkgs)
                        pkgs.python311Packages.python-lsp-server
                        pkgs.nodePackages.nodemon
                        pkgs.just
                    ];

                    shellHook = ''
                        echo Welcome to distributed systems shell
                    '';
                };
            }
        );
}
