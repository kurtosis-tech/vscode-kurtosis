package kurtosis

import (
	"context"
	_ "embed"
	"encoding/json"
	"fmt"
	"github.com/tilt-dev/starlark-lsp/pkg/docstring"
	"github.com/tilt-dev/starlark-lsp/pkg/query"
	"go.uber.org/zap"
)

//go:embed resource/kurtosis_type.json
var jsonFile []byte

type PluginWrapper struct {
	symbols    []query.Symbol
	signatures map[string]query.Signature
	members    []query.Symbol
	methods    map[string]query.Signature
}

type PluginContract struct {
	Name          string `json:"name"`
	Detail        string `json:"detail"`
	Documentation string `json:"documentation"`
	ReturnType    string `json:"returnType"`
	Params        []struct {
		Name         string `json:"name"`
		Type         string `json:"type"`
		Content      string `json:"content"`
		DefaultValue string `json:"defaultValue"`
		Detail       string `json:"detail"`
	} `json:"params"`
}

type PluginBuiltins struct {
	TypeBuiltIns   []PluginContract `json:"type_builtins"`
	MethodBuiltIns []PluginContract `json:"method_builtins"`
}

type PluginBuiltinProvider struct {
	logger         *zap.Logger
	pluginBuiltins PluginBuiltins
}

// this method is the main method which converts our definition into types recognized by starlark lsp
func (definition *PluginBuiltinProvider) convertToLSP() PluginWrapper {
	var symbols []query.Symbol
	signatures := make(map[string]query.Signature)

	for _, plugin := range definition.pluginBuiltins.TypeBuiltIns {
		// query symbol
		symbol := query.Symbol{
			Name:          plugin.Name,
			Detail:        plugin.Detail,
			Documentation: plugin.Documentation,
			KType:         true,
		}

		var signatureParams []query.Parameter
		var docStringFields []docstring.Field

		for _, param := range plugin.Params {
			signatureParam := query.Parameter{
				Name:         param.Name,
				TypeHint:     param.Type,
				DefaultValue: param.DefaultValue,
				Content:      fmt.Sprintf("%v:%v", param.Content, param.Type),
			}

			signatureParams = append(signatureParams, signatureParam)
			docstringField := docstring.Field{Name: param.Name, Desc: param.Detail}
			docStringFields = append(docStringFields, docstringField)
		}

		parsed := docstring.Parsed{
			Description: "",
			Fields: []docstring.FieldsBlock{
				{
					Title:  "Args",
					Fields: docStringFields,
				},
			},
		}

		signature := query.Signature{
			Name:       plugin.Name,
			Params:     signatureParams,
			ReturnType: plugin.ReturnType,
			Docs:       parsed,
		}
		symbols = append(symbols, symbol)
		signatures[plugin.Name] = signature
	}

	var members []query.Symbol
	methods := make(map[string]query.Signature)
	for _, plugin := range definition.pluginBuiltins.MethodBuiltIns {
		// query symbol
		member := query.Symbol{
			Name:          plugin.Name,
			Detail:        plugin.Detail,
			Documentation: plugin.Documentation,
			KType:         true,
		}

		var signatureParams []query.Parameter
		var docStringFields []docstring.Field

		for _, param := range plugin.Params {
			signatureParam := query.Parameter{
				Name:         param.Name,
				TypeHint:     param.Type,
				DefaultValue: param.DefaultValue,
				Content:      fmt.Sprintf("%v:%v", param.Content, param.Type),
			}

			signatureParams = append(signatureParams, signatureParam)
			docstringField := docstring.Field{Name: param.Name, Desc: param.Detail}
			docStringFields = append(docStringFields, docstringField)
		}

		parsed := docstring.Parsed{
			Description: "",
			Fields: []docstring.FieldsBlock{
				{
					Title:  "Args",
					Fields: docStringFields,
				},
			},
		}

		method := query.Signature{
			Name:       plugin.Name,
			Params:     signatureParams,
			ReturnType: plugin.ReturnType,
			Docs:       parsed,
		}
		members = append(members, member)
		methods[plugin.Name] = method
	}

	return PluginWrapper{
		symbols:    symbols,
		signatures: signatures,
		methods:    methods,
		members:    members,
	}
}

func (definition *PluginBuiltinProvider) ReadJsonFile(ctx context.Context) {
	//path, _ := os.Getwd()
	//pathToKurtosisType := filepath.Join(path, "pkg", "kurtosis", "resource", "kurtosis_type.json")

	// read our opened xmlFile as a byte array.

	var pluginBuiltIns PluginBuiltins
	err := json.Unmarshal(jsonFile, &pluginBuiltIns)
	if err != nil {
		definition.logger.Error(err.Error())
	}

	definition.pluginBuiltins = pluginBuiltIns
}
