/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */

import { ChildProcess, spawn } from "child_process"

import { workspace, ExtensionContext } from 'vscode';

import {
	LanguageClient,
	LanguageClientOptions,
	StreamInfo
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: ExtensionContext) {	
	// Options to control the language client
	const clientOptions: LanguageClientOptions = {
		// Register the server for plain text documents
		documentSelector: [{ scheme: 'file', language: 'starlark'}],
		synchronize: {
			// Notify the server about file changes to '.clientrc files contained in the workspace
			fileEvents: workspace.createFileSystemWatcher('**.star')
		}
	};

	// Create the language client and start the client.
	client = new LanguageClient(
		"kurtosis_lsp",
		'kurtosis_lsp',
		() => startServer(),
		clientOptions
	);

	// Start the client. This will also launch the server
	client.start();
}

export function deactivate(): Thenable<void> | undefined {
	if (!client) {
		return undefined;
	}
	return client.stop();
}

async function startServer(): Promise<ChildProcess | StreamInfo> {
	return spawn("starlark-lsp", ["start","--address=",":8567"])
}



