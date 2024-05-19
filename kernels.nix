{pkgs, ...}: {
  kernel.python.minimal = {
    enable = true;
  };
  kernel.python.qiskit-python = {
    enable = true;
    projectDir = ./my-custom-python;
  };
}
