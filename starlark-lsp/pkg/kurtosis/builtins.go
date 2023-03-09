package kurtosis

import (
	"context"
	"github.com/kurtosis-tech/vscode-kurtosis/starlark-lsp/pkg/analysis"
	"go.lsp.dev/protocol"
)

func GetKurtosisBuiltIn(ctx context.Context) *analysis.Builtins {
	logger := protocol.LoggerFromContext(ctx)

	provider := PluginBuiltinProvider{
		logger: logger,
	}

	provider.ReadJsonFile(ctx)
	converted := provider.convertToLSP()

	builtIn := analysis.NewBuiltins()
	builtIn.Symbols = converted.symbols
	builtIn.Functions = converted.signatures
	builtIn.Methods = converted.methods
	builtIn.Members = converted.members
	return builtIn
}
