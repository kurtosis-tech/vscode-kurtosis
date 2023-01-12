package server

import (
	"context"
	"fmt"

	"go.lsp.dev/protocol"
	"go.uber.org/zap"
)

func (s *Server) SignatureHelp(ctx context.Context,
	params *protocol.SignatureHelpParams) (*protocol.SignatureHelp, error) {
	logger := protocol.LoggerFromContext(ctx).
		With(textDocumentFields(params.TextDocumentPositionParams)...)

	doc, err := s.docs.Read(ctx, params.TextDocument.URI)
	if err != nil {
		return nil, err
	}
	defer doc.Close()

	zap.String("params", fmt.Sprintf("%+v", params))
	resp := s.analyzer.SignatureHelp(doc, params.Position)
	if resp != nil && len(resp.Signatures) != 0 {
		logger.With(
			zap.Namespace("signature"),
			zap.String("label", resp.Signatures[0].Label),
			zap.String("body", fmt.Sprintf("%+v", resp.Signatures[0])),
		).Info("found signature candidate")
	} else {
		logger.Debug("no signature found")
	}
	return resp, nil
}
