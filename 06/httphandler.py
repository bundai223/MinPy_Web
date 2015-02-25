#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Response(object):
    """
    Httpのレスポンスをハンドリングするクラス
    レスポンスを送る前にインスタンスを生成して利用する
    レスポンスやヘッダの内容の保持、ヘッダを含めたレスポンスの送信を行う
    """
    def __init__(self, charset='utf-8'):
        """
        インスタンスの初期化
        ヘッダ用の辞書、本文用の文字列を初期化する
        """
        self.headers = {'Content-type': 'text/html;charset=%s' % charset}
        self.body = ""
        self.status = 200
        self.status_message = ''

    def set_header(self, name, value):
        """
        レスポンスのヘッダを設定する
        """
        self.headers[name] = value

    def get_header(self, name):
        """
        設定済のレスポンス用ヘッダを返す
        """
        return self.headers.get(name, None)

    def set_body(self, bodystr):
        """
        レスポンスとして出力する文字列を返す
        """
