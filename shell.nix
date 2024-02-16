let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = { allowUnfree = true; }; overlays = []; };
in

pkgs.mkShell {
  packages = with pkgs; [
    python311
    python311Packages.pip
    pkgs.pdm
  ];

}