.class public Lcom/example/vaidhyesh/xiomaractf/MainActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "MainActivity.java"


# static fields
.field static myurl:Ljava/lang/String;

.field static query1:Ljava/lang/String;


# direct methods
.method static constructor <clinit>()V
    .locals 1

    .prologue
    .line 19
    const-string/jumbo v0, "http://103.5.112.91/2c3fa05a103d78ccf08c4df3c00dedda.php"

    sput-object v0, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->myurl:Ljava/lang/String;

    .line 20
    const-string/jumbo v0, "apikey"

    sput-object v0, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->query1:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>()V
    .locals 0

    .prologue
    .line 18
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V

    return-void
.end method

.method public static buildUrl(Ljava/lang/String;)Ljava/net/URL;
    .locals 6
    .param p0, "Query1"    # Ljava/lang/String;

    .prologue
    .line 77
    sget-object v4, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->myurl:Ljava/lang/String;

    invoke-static {v4}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v4

    invoke-virtual {v4}, Landroid/net/Uri;->buildUpon()Landroid/net/Uri$Builder;

    move-result-object v4

    sget-object v5, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->query1:Ljava/lang/String;

    .line 78
    invoke-virtual {v4, v5, p0}, Landroid/net/Uri$Builder;->appendQueryParameter(Ljava/lang/String;Ljava/lang/String;)Landroid/net/Uri$Builder;

    move-result-object v4

    .line 79
    invoke-virtual {v4}, Landroid/net/Uri$Builder;->build()Landroid/net/Uri;

    move-result-object v0

    .line 80
    .local v0, "builtUri":Landroid/net/Uri;
    const/4 v2, 0x0

    .line 82
    .local v2, "url":Ljava/net/URL;
    :try_start_0
    new-instance v3, Ljava/net/URL;

    invoke-virtual {v0}, Landroid/net/Uri;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-direct {v3, v4}, Ljava/net/URL;-><init>(Ljava/lang/String;)V
    :try_end_0
    .catch Ljava/net/MalformedURLException; {:try_start_0 .. :try_end_0} :catch_0

    .end local v2    # "url":Ljava/net/URL;
    .local v3, "url":Ljava/net/URL;
    move-object v2, v3

    .line 87
    .end local v3    # "url":Ljava/net/URL;
    .restart local v2    # "url":Ljava/net/URL;
    :goto_0
    return-object v2

    .line 83
    :catch_0
    move-exception v1

    .line 84
    .local v1, "e":Ljava/net/MalformedURLException;
    invoke-virtual {v1}, Ljava/net/MalformedURLException;->printStackTrace()V

    goto :goto_0
.end method

.method public static getResponseFromHttpUrl(Ljava/net/URL;)Ljava/lang/String;
    .locals 5
    .param p0, "url"    # Ljava/net/URL;
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/io/IOException;
        }
    .end annotation

    .prologue
    .line 59
    invoke-virtual {p0}, Ljava/net/URL;->openConnection()Ljava/net/URLConnection;

    move-result-object v3

    check-cast v3, Ljava/net/HttpURLConnection;

    .line 61
    .local v3, "urlConnection":Ljava/net/HttpURLConnection;
    :try_start_0
    invoke-virtual {v3}, Ljava/net/HttpURLConnection;->getInputStream()Ljava/io/InputStream;

    move-result-object v1

    .line 63
    .local v1, "in":Ljava/io/InputStream;
    new-instance v2, Ljava/util/Scanner;

    invoke-direct {v2, v1}, Ljava/util/Scanner;-><init>(Ljava/io/InputStream;)V

    .line 64
    .local v2, "scanner":Ljava/util/Scanner;
    const-string/jumbo v4, "\\A"

    invoke-virtual {v2, v4}, Ljava/util/Scanner;->useDelimiter(Ljava/lang/String;)Ljava/util/Scanner;

    .line 65
    invoke-virtual {v2}, Ljava/util/Scanner;->hasNext()Z

    move-result v0

    .line 66
    .local v0, "hasInput":Z
    if-eqz v0, :cond_0

    .line 67
    invoke-virtual {v2}, Ljava/util/Scanner;->next()Ljava/lang/String;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    move-result-object v4

    .line 73
    invoke-virtual {v3}, Ljava/net/HttpURLConnection;->disconnect()V

    .line 69
    :goto_0
    return-object v4

    :cond_0
    const/4 v4, 0x0

    .line 73
    invoke-virtual {v3}, Ljava/net/HttpURLConnection;->disconnect()V

    goto :goto_0

    .end local v0    # "hasInput":Z
    .end local v1    # "in":Ljava/io/InputStream;
    .end local v2    # "scanner":Ljava/util/Scanner;
    :catchall_0
    move-exception v4

    invoke-virtual {v3}, Ljava/net/HttpURLConnection;->disconnect()V

    throw v4
.end method


# virtual methods
.method public final md5()Ljava/lang/String;
    .locals 12

    .prologue
    .line 37
    const v8, 0x7f0b0020

    invoke-virtual {p0, v8}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->getString(I)Ljava/lang/String;

    move-result-object v7

    .line 38
    .local v7, "s":Ljava/lang/String;
    const-string/jumbo v0, "MD5"

    .line 40
    .local v0, "MD5":Ljava/lang/String;
    :try_start_0
    const-string/jumbo v8, "MD5"

    .line 41
    invoke-static {v8}, Ljava/security/MessageDigest;->getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;

    move-result-object v2

    .line 42
    .local v2, "digest":Ljava/security/MessageDigest;
    invoke-virtual {v7}, Ljava/lang/String;->getBytes()[B

    move-result-object v8

    invoke-virtual {v2, v8}, Ljava/security/MessageDigest;->update([B)V

    .line 43
    invoke-virtual {v2}, Ljava/security/MessageDigest;->digest()[B

    move-result-object v6

    .line 44
    .local v6, "messageDigest":[B
    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    .line 45
    .local v5, "hexString":Ljava/lang/StringBuilder;
    array-length v9, v6

    const/4 v8, 0x0

    :goto_0
    if-ge v8, v9, :cond_1

    aget-byte v1, v6, v8

    .line 46
    .local v1, "aMessageDigest":B
    and-int/lit16 v10, v1, 0xff

    invoke-static {v10}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v4

    .line 47
    .local v4, "h":Ljava/lang/String;
    :goto_1
    invoke-virtual {v4}, Ljava/lang/String;->length()I

    move-result v10

    const/4 v11, 0x2

    if-ge v10, v11, :cond_0

    .line 48
    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string/jumbo v11, "0"

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_1

    .line 49
    :cond_0
    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    .line 45
    add-int/lit8 v8, v8, 0x1

    goto :goto_0

    .line 51
    .end local v1    # "aMessageDigest":B
    .end local v4    # "h":Ljava/lang/String;
    :cond_1
    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    :try_end_0
    .catch Ljava/security/NoSuchAlgorithmException; {:try_start_0 .. :try_end_0} :catch_0

    move-result-object v8

    .line 56
    .end local v2    # "digest":Ljava/security/MessageDigest;
    .end local v5    # "hexString":Ljava/lang/StringBuilder;
    .end local v6    # "messageDigest":[B
    :goto_2
    return-object v8

    .line 53
    :catch_0
    move-exception v3

    .line 54
    .local v3, "e":Ljava/security/NoSuchAlgorithmException;
    invoke-virtual {v3}, Ljava/security/NoSuchAlgorithmException;->printStackTrace()V

    .line 56
    const-string/jumbo v8, ""

    goto :goto_2
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 7
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 23
    invoke-super {p0, p1}, Landroid/support/v7/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 24
    const v4, 0x7f09001b

    invoke-virtual {p0, v4}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->setContentView(I)V

    .line 25
    invoke-virtual {p0}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->md5()Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->buildUrl(Ljava/lang/String;)Ljava/net/URL;

    move-result-object v2

    .line 27
    .local v2, "u":Ljava/net/URL;
    :try_start_0
    invoke-static {v2}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->getResponseFromHttpUrl(Ljava/net/URL;)Ljava/lang/String;

    move-result-object v1

    .line 28
    .local v1, "response":Ljava/lang/String;
    const v4, 0x7f070045

    invoke-virtual {p0, v4}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v3

    check-cast v3, Landroid/widget/TextView;

    .line 29
    .local v3, "v":Landroid/widget/TextView;
    invoke-virtual {v3, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0

    .line 35
    .end local v1    # "response":Ljava/lang/String;
    .end local v3    # "v":Landroid/widget/TextView;
    :goto_0
    return-void

    .line 30
    :catch_0
    move-exception v0

    .line 31
    .local v0, "e":Ljava/io/IOException;
    const-string/jumbo v4, "Dev logs!"

    const-string/jumbo v5, "Noob dev !Fix the bug."

    invoke-static {v4, v5}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 32
    invoke-virtual {p0}, Lcom/example/vaidhyesh/xiomaractf/MainActivity;->getApplicationContext()Landroid/content/Context;

    move-result-object v4

    const-string/jumbo v5, "Dev is noob bro!!"

    const/4 v6, 0x0

    invoke-static {v4, v5, v6}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v4

    invoke-virtual {v4}, Landroid/widget/Toast;->show()V

    goto :goto_0
.end method
