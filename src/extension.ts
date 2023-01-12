/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 * ------------------------------------------------------------------------------------------ */

import net = require("net")
import { ChildProcess, spawn } from "child_process"

import * as path from 'path';
import { workspace, ExtensionContext, window } from 'vscode';

import {
	LanguageClient,
	LanguageClientOptions,
	ServerOptions,
	StreamInfo,
	TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: ExtensionContext) {
	// The server is implemented in node
	const file = context.asAbsolutePath(
		path.join('execute.sh')
	);

	// const logFile = context.asAbsolutePath(
	// 	path.join('debugger.txt')
	// );

	// If the extension is launched in debug mode then the debug server options are used
	// Otherwise the run options are used
	const serverOptions: ServerOptions = {
		run: {command: "bash", args: [file]},
		debug: {command: "bash", args: [file]}
	};

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
		() => startServer(file),
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

async function startServer(command: string): Promise<ChildProcess | StreamInfo> {
	// console.log("Starting Serverrr")
	// if (command !== "") {
	// 	const process = spawn(command)
	// 	process.on("connection", () => {
	// 		console.log("someone connected")
	// 	})
	// 	console.log("PROCESS", process)
	// 	process.stdout.on( 'data', 
	// 		data => console.log( data ) 
	// 	);

	// }

	// const socket = net.connect({ host: "0.0.0.0", port:8567 })
	// return { writer: socket, reader: socket }
	console.log(process.env)
	return spawn("starlark-lsp", ["start","--address=",":8567"])
}
	

// /* --------------------------------------------------------------------------------------------
//  * Copyright (c) Microsoft Corporation. All rights reserved.
//  * Licensed under the MIT License. See License.txt in the project root for license information.
//  * ------------------------------------------------------------------------------------------ */
// import * as vscode from 'vscode';
// import net = require("net")
// import { ChildProcess, spawn } from "child_process"

// import {
// 	LanguageClient,
// 	LanguageClientOptions, 
// 	StreamInfo
// } from 'vscode-languageclient/node';


// let client: LanguageClient;

// export function activate(context: vscode.ExtensionContext) {
// 	// Options to control the language client
// 	const clientOptions: LanguageClientOptions = {
// 		// Register the server for plain text documents
// 		documentSelector: [{ scheme: 'file', language: 'starlark' }],
// 		synchronize: {
// 			// Notify the server about file changes to '.clientrc files contained in the workspace
// 			fileEvents: vscode.workspace.createFileSystemWatcher('**.star'),
// 		}
// 	};

// 	// Create the language client and start the client.
// 	client = new LanguageClient(
// 		'languageServerExample',
// 		'Language Server Example PK',
// 		() => startServer(),
// 		clientOptions,
// 	);

// 	// Start the client. This will also launch the server
	
// 	client.start();
// }

// export function deactivate(): Thenable<void> | undefined {
// 	if (!client) {
// 		return undefined;
// 	}
// 	return client.stop();
// }



