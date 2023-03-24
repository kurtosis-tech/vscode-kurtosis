package analysis

import (
	"testing"

	"github.com/stretchr/testify/require"
	"go.lsp.dev/protocol"
)

func TestBuiltinDefinition(t *testing.T) {
	f := newFixture(t)
	f.AddSymbol("import_module", "foo")
	doc := f.MainDoc("import_module()")
	result := f.a.Definition(f.ctx, doc, protocol.Position{Character: 3})
	require.Len(t, result, 0)
}
