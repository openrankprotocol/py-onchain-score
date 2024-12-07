# openrank-onchain-score

A package and CLI to manage OpenRank scores published onchain.

Currently supports reading and managing OpenRank Farcaster global trust onchain.

## Quickstart

Set up a Python 3.10+ virtualenv, then inside it:

```
$ pip install openrank-onchain-score
$ openrank-onchain-score --help

 Usage: openrank-onchain-score [OPTIONS] COMMAND [ARGS]...

╭─ Options ───────────────────────────────────────────────────────────────────╮
│ --chain                                 NAME     target chain               │
│                                                  [default: base]            │
│ --contract                              ADDRESS  score contract address     │
│                                                  [default: (chain default)] │
│ --abi                                   TEXT     contract ABI name          │
│                                                  [default: v1]              │
│ --rpc                                   URI      JSON-RPC endpoint          │
│                                                  [default: (chain default)] │
│ --dry-run               --no-dry-run             dry-run write transactions │
│                                                  (just print gas estimate)  │
│                                                  [default: no-dry-run]      │
│ --log-level                             NAME     logging level, e.g. debug, │
│                                                  info, warning              │
│                                                  [default: warning]         │
│ --install-completion                             Install completion for the │
│                                                  current shell.             │
│ --show-completion                                Show completion for the    │
│                                                  current shell, to copy it  │
│                                                  or customize the           │
│                                                  installation.              │
│ --help                                           Show this message and      │
│                                                  exit.                      │
╰─────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ length              Print the number of entries in the leaderboard.         │
│ get-score-at-rank   Print the FID and the OpenRank score at the given rank  │
│                     (1-based).                                              │
│ get-rank-for-fid    Print the 1-based rank of the given FID.                │
│ truncate            Truncate leaderboard.                                   │
│ upload-from-csv     Upload scores from a CSV file.                          │
│ version             Print the version number.                               │
╰─────────────────────────────────────────────────────────────────────────────╯

$ # dummy key for read-only operations, Anvil test key 0
$ export WEB3_KEY='ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
$ openrank-onchain-score length
51000
$ openrank-onchain-score get-rank-for-fid 2148  # yours truly :)
34843
$ openrank-onchain-score get-score-at-rank 34843
2148 5.9470017e-07
$ openrank-onchain-score get-score-at-rank --raw 34843
2148 68861575154087109397824182927854231026949096349334030660271211628462080
```
