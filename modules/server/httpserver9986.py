import os
import time
import datetime
import random
"import specifed class from module BaseHTTPSever"
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

'''
author YangYun
modified ShaoCheng
version 1.0
time 2015-8-17
'''

'''
function - Get_Content_Length()
description - return sample data according to length.
parameter - length, the length specified in url.
'''
def Get_Content_Length(length):
    str = '1234567890'
    a = length/10
    b = length%10
    #    str_ret = ''
    #    for i in range(a):
    #    str_ret += str
    "use the next line to substitue above three lines, because simple"
    str_ret = str*a
    str_ret += str[:b]
    return str_ret

'''
function - Get_Body()
descprion - return a tuple contains sample data and its length.
parameter - path, url path
'''
def Get_Body(path):
    if '?length=' in path:
        split = path.split('?length=')
    else:
        path_tmp = '/a1?length=23'
        split = path_tmp.split('?length=')
    length = 0
    find = False
    for i in split[1]:
        if i>='0' and i<='9':
            length = length*10+int(i)
        else:
            find = True
        if find == True:
            break;
    body = Get_Content_Length(length)
    return (body,length)

'''
description - decode range request if a url contains range, return a tuple that contains
    such as (3, 18)
'''
def Decode_Range(str):
    range = str.split('=')[1]
    start = range.split('-')[0]
    end = range.split('-')[1]
    if start == None and end == None:
        return (None, None)
    if start == None:
        return (None, int(end))
    if end == None:
        return (int(start), None)
    return (int(start), int(end))

def Docode_HTTP_Date(str):
    try:
        return datetime.datetime.strptime(str,"%a,%d %b %Y %H:%M:%S GMT")
    except:
        return None

def Encode_HTTP_Date(time):
    try:
        return datetime.datetime.strftime(bb,"%a,%d %b %Y %H:%M:%S GMT")
    except:
        return None

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        "BaseHTTPRequestHandler has instance variables: path - uri path"
        path = self.path
        self.protocol_version = 'HTTP/1.1'
        file1=open('./checklog','a')
        file1.write('8801 ')
        file1.write(path+'\n')
        file1.close()
        if path[:8] == '/opencdn':
            return self.Back_Opencdn()
        if path[:9] == '/range404':
            return self.Get_Range404()
        if path[:9] == '/range200':
            return self.Get_Range200()
        if path[:9] == '/range444':
            return self.Get_Range444()
        if path[:10] == '/range_404':
            return self.Get_Range_404()
        if path[:10] == '/range_206':
            return self.Get_Range_206()
        if path[:10] == '/range_444':
            return self.Get_Range_444()
        if path[:10] == '/errlength':
            return self.Get_Err_ContentLength()
        if path[:8] == '/errhead':
            return self.Get_ErrHead()
        if path[:8] == '/sepbody':
            return self.Get_Sep_Body()
        if path[:7] == '/modify':
            return self.Get_Modify()
        if path[:8] == '/lmodify':
            return self.Get_LModify()
        if path[:11] == '/newlmodify':
            return self.Get_NewLModify()
        if path[:11] == '/lastmodify':
            return self.Get_LastModify()
        if path[:5]== '/conn':
            return self.Get_Connection()
        if path[:8] == '/expires':
            return self.Get_Mul_Expires()
        if path[:7] == '/expire':
            return self.Get_Expire()
        if path[:6] == '/cache':
            return self.Get_CacheControl()
        if path[:7] == '/maxage':
            return self.Get_MaxAge()
        if path[:10] == '/conencode':
            return self.Get_Content_Encoding()
        if path[:8] == '/codeerr':
            return self.Get_CodeErr()
        if path[:4] == '/err':
            return self.Get_Err()
        if path[:13] == '/nolensepbody':
            return self.Get_NoLenSepBody()
        if path[:6] == '/nolen':
            return self.Get_NoLen()
        if path[:7] == '/nobody':
            return self.Get_Nobody()
        if path[:7] == '/cnolen':
            return self.Get_Nolen_Chunk()
        if path[:5] == '/wait':
            return self.Get_Wait()
        if path[:7] == '/cookie':
            return self.Get_CookieandP3p()
        if path[:8] == '/trunked':
            return self.Get_Trunked()
        if path[:5] == '/file':
            return self.Get_File()
        if path[:9] == '/longhead':
            return self.Get_LongHead()
        if path[:8] == '/rencode':
            return self.Get_Range_Encoding()
        if path[:4] == '/via':
            return self.Get_Via()
        if path[:9] == '/testurls':
            return self.Test_urls()
        if path[:3] == '/t1':
            return self.testxb(1)
        if path[:3] == '/t2':
            return self.testxb(2)
        if path[:3] == '/t3':
            return self.testxb(3)
        if path[:3] == '/t4':
            return self.testxb(4)
        if path[:3] == '/t5':
            return self.testxb(5)
        if path[:3] == '/t6':
            return self.testxb(6)
        if path[:3] == '/t7':
            return self.testxb(7)
        if path[:4] == '/p3p':
            return self.p3p()
        if path[:11] == '/set-cookie':
            return self.set_cookie()
        if path[:13] == '/lastmodifyxb':
            return self.lmodifyxb()
        return self.Get_Normal()

    def lmodifyxb(self):
        path = self.path
        body, len = Get_Body(path)
        self.send_response(200)
        self.send_header('Content-Length','123')
        #self.send_header('last-modified','123456')
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def p3p(self):
        path = self.path
        body, len = Get_Body(path)

        self.send_response(200)
        self.send_header('Content-Length','%d' % len)
        #self.send_header('Content-Length','-1')
        self.send_header('p3p', '123')
        self.end_headers()

        self.wfile.write(body)
        self.wfile.close()

    def set_cookie(self):
        path = self.path
        body, len = Get_Body(path)

        self.send_response(200)
        self.send_header('Content-Length','%d' % len)
        self.send_header('set-cookie','123')
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def testxb(self,index):
        path = self.path
        body,len = Get_Body(path)
        if index == 1:
            self.send_response(206)
        if index == 2:
            self.send_response(400)
        if index == 3:
            self.send_response(401)
        if index == 4:
            self.send_response(404)
        if index == 5:
            self.send_response(502)
        if index == 6:
            self.send_response(504)
        if index == 7:
            self.send_response(888)
        self.send_header('Content-Length','%d' % len)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def Test_urls(self):
        path = self.path
        #body,length = Get_Body(path)
        time.sleep(5)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        #self.send_header('content-Length','%d'%(length))
        #self.send_header('X-bs-meta-crc32','')
        #self.send_header('Age','1')
        self.send_header('x-bs-meta-crc32','0x1da1251b')
        #self.send_header('cache-control','private')
        #self.send_header('name','yangyun')
        self.send_header('Etag','"5421182c79e4794397b1e608e529827d"')
        #self.send_header('Pragma','no-')
        #self.send_header('self-test','1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234')
        cur_time = datetime.datetime.utcnow()
        time1 = cur_time + datetime.timedelta(seconds=5)
        str_time = datetime.datetime.strftime(time1,"%a,, %d, %b %Y %H:%M:%S +0800")
        #str_time = 'Wed,16 '+datetime.datetime.strftime(time,"%b %Y %H:%M:%S GMT")
        self.send_header('Expires',str_time)
        self.end_headers()
        #self.wfile.write(body)
        self.wfile.write('sajdkasjdklajsdl')
        self.wfile.close()
        return

    def Back_Opencdn(self):
        self.send_response(200)
        len = 155
        self.send_header('Content-Type','text/html')
        self.send_header('Content-Length','%d'%len)
        self.end_headers()
        self.wfile.write("	{\"error_code\":0,\"version\":5,\"oldversion\":\"2\",\"number\":1,\"content\":[{\"host\":\"abc.jomodns.com\",\"userId\":\"XFTHM7XKK98IBGAR8E8JTKIT0WSTS175\",\"action\":\"add\"}]}")
        self.wfile.close()
        return

    def Get_Normal(self):
        path = self.path
        body,length = Get_Body(path)
        #time.sleep(6);
        #age = 60
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        self.send_header('Name','####9986####')
        #self.send_header('Cache-control','max-age=10')
        #self.send_header('x-bs-meta-crc32','639479525')
        #self.send_header('Cache-control','no-cache')
        #self.send_header('Location','www.baidu')
        #self.send_header('ETag',"\"abcdb\"")
        self.end_headers()
        #time.sleep(2)
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_CodeErr(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        para = path.split('code=')[1]
        self.send_response(int(para),"")
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def Get_Errorre(self):
        path = self.path
        body,length = Get_Body(path)
        self.send_response(206,)
        self.end_headers()
        self.wfile.close()
        return

    def Get_Via(self):
        path = self.path
        body,length = Get_Body(path)
        self.send_response(200)
        self.send_header('Via','via-aabb.baidu.com')
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_Range(self,start,end):
        path = self.path
        split = path.split('?length=')
        length = int(split[1])
        if start == None and end != None:
            length = end
        if start != None and end == None:
            length -= start
        if start != None and end != None:
            length = end - start
        body = Get_Content_Length(length)
        self.send_response(206,)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%len(body))
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_Range404(self):
        header = self.headers
        if None != header.get('Range'):
            self.send_response(404)
            self.end_headers()
            return
        return self.Get_Normal()

    def Get_Range200(self):
        return self.Get_Normal()

    def Get_Range444(self):
        header = self.headers
        if None != header.get('Range'):
            return
        return self.Get_Normal()

    def Get_Range_404(self):
        header = self.headers
        value = header.get('Range')
        if None != value:
            start,end=Decode_Range(value)
            return self.Get_Range(start,end)
        self.send_response(404)
        self.end_headers()
        return

    def Get_Range_206(self):
        header = self.headers
        value = header.get('Range')
        if None != value:
            start,end=Decode_Range(value)
            return self.Get_Range(start,end)
        return self.Get_Range(None,None)

    def Get_Range_444(self):
        header = self.headers
        value = header.get('Range')
        if None != value:
            start,end=Decode_Range(value)
            return self.Get_Range(start,end)
        return

    def Get_Err_ContentLength(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        ret_length = int(path.split('retlen=')[1])
        self.send_response(200)
        self.send_header('Content-type','text/html')
        if ret_length != -1:
            self.send_header('Content-Length','%d'%ret_length)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_Sep_Body(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        para1 = path.split('retlen=')[1]
        ret_len = int(para1.split('part2=')[0])
        para2 = para1.split('part2=')[1]
        length2 = int(para2.split('time=')[0])
        times = int(para1.split('time=')[1])
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%ret_len)
        self.end_headers()
        self.wfile.write(body)
        time.sleep(times)
        body = Get_Content_Length(length2)
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_NoLenSepBody(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        para1 = path.split('part2=')[1]
        length2 = int(para1.split('time=')[0])
        times = int(para1.split('time=')[1])
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(body)
        time.sleep(times)
        body = Get_Content_Length(length2)
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_Modify(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        code = 200
        ori = header.get('if-modified-since')
        range = header.get('range')
        if None != range:
            start,end=Decode_Range(range)
            body = body[start:end]
            length = end-start
            code = 206
        self.send_response(code)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)

        ori_time = Docode_HTTP_Date(ori)
        try:
            day = int(path.split('day=')[1])
            out_time = ori_time + datetime.timedelta(days=day)
            out = datetime.datetime.strftime(out_time,"%a,%d %b %Y %H:%M:%S GMT")
            self.send_header('Last-Modified',out)
        except:
            print 'get date error'
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_LModify(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        code = 200
        range = header.get('range')
        if None != range:
            start,end=Decode_Range(range)
            body = body[start:end]
            length = end-start
            code = 206
        self.send_response(code)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        try:
            print 'aaa'
            day = int(path.split('time=')[1])
            print day
            time1 = datetime.datetime.now()
            print time1
            out_time = time1 + datetime.timedelta(days=day)
            print out_time
            out = datetime.datetime.strftime(out_time,"%a,%d %b %Y %H:%M:%S GMT")
            print out
            self.send_header('Last-Modified',out)
        except:
            print 'get date error'
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_NewLModify(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        ori = header.get('if-modified-since')
        print 'ori:',ori
        try:
            print 'aaa'
            day = int(path.split('time=')[1])
            print day
            time1 = datetime.datetime.now()
            print time1
            out_time = time1 + datetime.timedelta(days=day)
            print out_time
            out = datetime.datetime.strftime(out_time,"%a,%d %b %Y %H:%M:%S GMT")
            print out
            self.send_header('Last-Modified',out)
        except:
            print 'get date error'
        if ori=='Tue, 18 Jun 2013 12:33:12 GMT':
            code=304
            self.send_response(code)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.close()
        else:
            code=200
            self.send_response(code)
            self.send_header('Content-type','text/html')
            self.send_header('Content-Length','%d'%length)
            self.end_headers()
            self.wfile.write(body)
            self.wfile.close()
    def Get_LastModify(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        #print path
        try:
            last_modify = path.split('lmodify=')[1]
            last_modify = last_modify.replace('%20',' ')
            print last_modify
            self.send_header('Last-Modified',last_modify)
        except:
            print 'get last modified para error'
        #try:
        #    day = int(path.split('day=')[1])
        #    out_time = ori_time + datetime.timedelta(days=day)
        #    out = datetime.datetime.strftime(out_time,"%a,%d %b %Y %H:%M:%S GMT")
        #    self.send_header('Last-Modified',out)
        #except:
        #    print 'get date error'
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_Last_Modify(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)

        cur_time = datetime.datetime.now()
        parasA['if-modified-since'] = datetime.datetime.strftime(time1,"%a,%d %b %Y %H:%M:%S GMT")

        try:
            day = path.split('time=')[1]
            if day == 'sp':
                self.send_header('Last-Modified',' ')
            elif day == 'no':
                print 'no last modify'
            elif day == 'wf':
                self.send_header('Last-Modified','AABBCCD')
            else:
                add = int(day)
                time = cur_time + datetime.timedelta(days=add)
                str_time = datetime.datetime.strftime(time,"%a,%d %b %Y %H:%M:%S GMT")
                self.send_header('Last-Modified',str_time)
        except:
            print 'get date error'

        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def Get_Connection(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        connection = path.split('conn=')[1]
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        if connection != 'no':
            self.send_header('Connection','%s'%connection)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def Get_Expire(self):
        path = self.path
        body,length = Get_Body(path)
        para = path.split('time=')[1]
        self.send_response(200)
        self.send_header('Content-Length','%d'%length)
        self.send_header('Content-type','text/html')
        if para != 'no':
            sec = int(para)
            cur_time = datetime.datetime.utcnow()
            time = cur_time + datetime.timedelta(seconds=sec)
            str_time = datetime.datetime.strftime(time,"%a,%d %b %Y %H:%M:%S GMT")
            self.send_header('Expires',str_time)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def Get_CacheControl(self):
        path = self.path
        body,length = Get_Body(path)
        para = path.split('cache=')[1]
        self.send_response(200)
        self.send_header('Content-Length','%d'%length)
        self.send_header('Content-type','text/html')
        if para != 'no':
            self.send_header('Cache-Control','%s'%para)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_MaxAge(self):
        path = self.path
        body,length = Get_Body(path)
        para = path.split('mage=')[1]
        self.send_response(200)
        self.send_header('Content-Length','%d'%length)
        self.send_header('Content-type','text/html')
        if para != 'no':
            self.send_header('Cache-Control','max-age=%s'%para)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def Get_Mul_Expires(self):
        path = self.path
        body,length = Get_Body(path)
        para1 = path.split('exp=')[1]
        exp = para1.split('mage=')[0]
        mage = para1.split('mage=')[1]
        self.send_response(200)
        self.send_header('Content-Length','%d'%length)
        self.send_header('Content-type','text/html')
        if exp != 'no':
            sec = int(exp)
            cur_time = datetime.datetime.utcnow()
            time = cur_time + datetime.timedelta(seconds=sec)
            str_time = datetime.datetime.strftime(time,"%a,%d %b %Y %H:%M:%S GMT")
            self.send_header('Expires',str_time)
        if mage != 'no':
            self.send_header('Cache-Control','max-age=%s'%mage)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_Range_Encoding(self):
        path = self.path
        code = path.split('code=')[1]
        body,length = Get_Body(path)
        header = self.headers
        value = header.get('Range')
        value2 = header.get('Accept-Encoding')
        if None != value:
            start,end=Decode_Range(value)
            if start == None and end != None:
                length = end
            if start != None and end == None:
                length -= start
            if start != None and end != None:
                length = end - start
            self.send_response(206)
            self.send_header('Content-Range','bytes %d-%d'%(start,end))
        else:
            self.send_response(200)
        body = Get_Content_Length(length)
        if code != 'no' and None != value2:
            self.send_header('Content-Encoding','%s'%code)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%len(body))
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
        return

    def Get_Content_Encoding(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        para = path.split('code=')[1]
        try:
            code = para.split('mage=')[0]
            mage = para.split('mage=')[1]
        except:
            code = para
            mage = None

        if code == '404':
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.send_header('Content-Length','0')
            self.end_headers()
            self.wfile.close()
            return
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        if code != 'no':
            self.send_header('Content-Encoding','%s'%code)
            body='ABCDEFGHIK'
            if mage != None:
                self.send_header('Cache-Control','max-age=%s'%mage)
            self.end_headers()
            self.wfile.write(body)
            self.wfile.close()
            return
        if mage != None:
            self.send_header('Cache-Control','max-age=%s'%mage)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_Err(self):
        header = self.headers
        path = self.path
        para = path.split('code=')[1]
        self.send_response(int(para),'Test Error')
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','0')
        self.end_headers()
        self.wfile.close()
    def Get_NoLen(self):
        path = self.path
        body,length = Get_Body(path)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_Nobody(self):
        path = self.path
        body,length = Get_Body(path)
        para = path.split('len=')[1]
        self.send_response(200)
        if para == 'on':
            self.send_header('Content-Length','0')
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_Nolen_Chunk(self):
        path = self.path
        body,length = Get_Body(path)
        part = 3
        rand = 0
        tail = 1

        #self.send_response(200)
        self.send_response(302)
        self.send_header('Content-type','text/html')
        self.send_header('Transfer-encoding','chunked')
        self.end_headers()

        time.sleep(1)

        i = 0
        begin = 0
        end = 0
        part_len = length/part
        while i<part:
            if i == part-1:
                end = length
                lengthn = end - begin
            elif rand != 1:
                end = begin+part_len
                lengthn = part_len
            else:
                lengthn = random.randint(1,part_len)
                end = begin + lengthn
            bodyn = hex(lengthn)[2:] + '\r\n' + body[begin:(end)]  + '\r\n'
            begin = end
            self.wfile.write(bodyn)
            i = i+1
        if tail != 0:
            bodyn = '0\r\n\r\n'
            self.wfile.write(bodyn)
        self.wfile.close()
    def Get_Wait(self):
        path = self.path
        body,length = Get_Body(path)
        para = path.split('time=')[1]
        print 'wait %s seconds'%para
        time.sleep(int(para))
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_CookieandP3p(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        para = path.split('cookie=')[1]
        cookie = para.split('p3p=')[0]
        para1 = para.split('p3p=')[1]
        p3p = para1.split('cno=')[0]
        try:
            para2 = para1.split('cno=')[1]
            cno = int(para2.split('pno=')[0])
            pno = int(para2.split('pno=')[1])
        except:
            cno=1
            pno=1

        value = header.get('Range')
        if None != value:
            start,end=Decode_Range(value)
            if start == None and end != None:
                length = end
            if start != None and end == None:
                length -= start
            if start != None and end != None:
                length = end - start
            self.send_response(206)
            self.send_header('Content-Range','bytes %d-%d'%(start,end))
        else:
            self.send_response(200)
        body = Get_Content_Length(length)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%len(body))
        if cookie != 'no':
            for i in range(cno):
                self.send_header('Set-cookie','name=%s%d'%(cookie,i+1))
        if p3p != 'no':
            for i in range(pno):
                self.send_header('P3p','CP=\"%s%d\"'%(p3p,i+1))
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_Trunked(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        para = path.split('part=')[1]
        part = int(para.split('random=')[0])
        para2 = para.split('random=')[1]
        rand = int(para2.split('tail=')[0])
        tail = int(para2.split('tail=')[1])

        self.send_response(200)
        self.send_header('Content-type','text/html')
        #self.send_header('Content-length','16')
        self.send_header('Transfer-encoding','chunked')
        self.end_headers()

        i = 0
        begin = 0
        end = 0
        part_len = length/part
        while i<part:
            if i == part-1:
                end = length
                lengthn = end - begin
            elif rand != 1:
                end = begin+part_len
                lengthn = part_len
            else:
                lengthn = random.randint(1,part_len)
                end = begin + lengthn
            bodyn = hex(lengthn)[2:] + '\r\n'
            self.wfile.write(bodyn)
            #time.sleep(1)
            bodyn = body[begin:end]  + '\r\n'
            begin = end
            self.wfile.write(bodyn)
            i = i+1
        if tail != 0:
            #self.wfile.write('0')
            #time.sleep(1)
            bodyn = '0\r\n\r\n'
            self.wfile.write(bodyn)
        self.wfile.close()

    def Get_File(self):
        header = self.headers
        path = self.path
        para = path.split('file=')[1]
        file = 'files/'+para
        try:
            f = open(file,'r')
            length = os.stat(file).st_size
            print 'length='+str(length )
            self.send_response(200)
            self.send_header('Content-Length','%d'%length)
            self.end_headers()
            self.wfile.write(f.read())
        except:
            self.send_response(404)
            self.end_headers()
            return
    def Get_LongHead(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        hlen = int(path.split('hlen=')[1])
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        if hlen > 200:
            string = Get_Content_Length(hlen-200)
            self.send_header('Invalid-Header',string)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
    def Get_ErrHead(self):
        header = self.headers
        path = self.path
        body,length = Get_Body(path)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Content-Length','%d'%length)
        self.send_header('Errorhead','err')
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()
try:
    server = HTTPServer(('',9986),MyHandler)
    print 'started server...'
    server.serve_forever()
except KeyboardInterrupt:
    print 'shutting down'
    server.socket.close()
