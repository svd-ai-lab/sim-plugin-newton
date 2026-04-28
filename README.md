# sim-plugin-newton

Newton driver for [sim-cli](https://github.com/svd-ai-lab/sim-cli),
distributed as an out-of-tree plugin.

Newton driver for sim (v1: one-shot subprocess).

## Install

```bash
sim plugin install newton
```

Other paths:

```bash
pip install git+https://github.com/svd-ai-lab/sim-plugin-newton@v0.1.0
pip install https://github.com/svd-ai-lab/sim-plugin-newton/releases/download/v0.1.0/sim_plugin_newton-0.1.0-py3-none-any.whl
pip install -e .
```

After install:

```bash
sim plugin doctor newton
sim plugin sync-skills
```

## Development

```bash
git clone https://github.com/svd-ai-lab/sim-plugin-newton
cd sim-plugin-newton
uv sync
uv run pytest
```

## License

Apache-2.0.
