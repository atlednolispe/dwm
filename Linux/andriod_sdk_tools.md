Ubuntu18.04配置andriod环境
=========================

## 安装JDK

[jdk8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

jdk10不兼容andriod-sdk-tools

```
# atlednolispe @ ubuntu1804 in ~/Applications [16:30:10]
$ tar -zxvf jdk-8u171-linux-x64.tar.gz

$ vim ~/.zshrc
JAVA_HOME="/home/atlednolispe/Applications/jdk1.8.0_171"
PATH="$JAVA_HOME/bin:$PATH"
export PATH
```

## 安装andriod-sdk-tools

[Command line tools only](https://developer.android.com/studio/#downloads)

```
# atlednolispe @ ubuntu1804 in ~/Applications [16:30:10]
$ unzip sdk-tools-linux-3859397.zip

# 通过sdkmanager安装adb
# atlednolispe @ ubuntu1804 in ~/Applications/tools/bin [16:37:14] 
$ ./sdkmanager --list

# atlednolispe @ ubuntu1804 in ~/Applications/tools/bin [16:37:14] 
$ ./sdkmanager platform-tools

# atlednolispe @ ubuntu1804 in ~/Applications/tools/bin [16:37:14] 
$ sudo ln -s /home/atlednolispe/Applications/platform-tools/adb /usr/bin/adb
```

## 获取app相应信息

```
$ adb shell

shell@dior:/ $ dumpsys window windows | grep -E 'mCurrentFocus|FocusedApp'
  mCurrentFocus=Window{42a2f7f0 u0 com.facebook.katana/com.facebook.katana.LoginActivity}
  mFocusedApp=AppWindowToken{42b9a1f0 token=Token{42a50b18 ActivityRecord{42a90d10 u0 com.facebook.katana/.LoginActivity t2}}}
```
