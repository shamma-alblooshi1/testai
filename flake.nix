{
  description = "LangChain + OpenAI agent flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python311;
        pythonPackages = python.pkgs;

        nativeBuildInputs = with pythonPackages; [
          pip
          setuptools
          wheel
          virtualenv
        ];

        buildInputs = with pythonPackages; [
          langchain
          langchain-community
          langchain-core
          langchain-ollama
          openai
          tkinter
        ];
      in {
        devShells.default = pkgs.mkShell {
          inherit nativeBuildInputs buildInputs;

          shellHook = ''
            echo "✅ LangChain dev environment ready"
            echo "👉 Reminder: export OPENAI_API_KEY=your_key_here"

  if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Starting Ollama..."
    nohup ollama serve > /tmp/ollama.log 2>&1 &
    sleep 2
  fi

  if ! ollama show mistral >/dev/null 2>&1; then
    echo "Pulling model 'mistral'..."
    ollama pull mistral
            fi
          '';
        };

        packages.default = pythonPackages.buildPythonApplication {
          pname = "ai-agent";
          version = "0.1.0";
          format = "setuptools";
          src = ./.;
          doCheck = false;
          inherit nativeBuildInputs buildInputs;
        };
      });
}