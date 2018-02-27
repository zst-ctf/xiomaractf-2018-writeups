# Mario Mystery
Reverse Engineering - 50 points

## Challenge 
> Young Mario was playing around with Android and wrongly built his app and crashed his app. Help him recover the flag he put in his server.

> [Xiomara_2k18.apk](Xiomara_2k18.apk)

## Solution

### Source code

Decompile android app

	$ apktool d ./Xiomara_2k18.apk -o Xiomara_2k18
	$ dex2jar ./Xiomara_2k18.apk 

Open in JD-GUI

In MainActivity.java

	protected void onCreate(Bundle paramBundle)
	  {
	    super.onCreate(paramBundle);
	    setContentView(2131296283);
	    paramBundle = buildUrl(md5());
	    try
	    {
	      paramBundle = getResponseFromHttpUrl(paramBundle);
	      ((TextView)findViewById(2131165253)).setText(paramBundle);
	      return;
	    }
	    catch (IOException paramBundle)
	    {
	      Log.e("Dev logs!", "Noob dev !Fix the bug.");
	      Toast.makeText(getApplicationContext(), "Dev is noob bro!!", 0).show();
	    }
	  }

	public static URL buildUrl(String paramString)
	  {
	    paramString = Uri.parse(myurl).buildUpon().appendQueryParameter(query1, paramString).build();
	    try
	    {
	      paramString = new URL(paramString.toString());
	      return paramString;
	    }
	    catch (MalformedURLException paramString)
	    {
	      paramString.printStackTrace();
	    }
	    return null;
	  }

We also need these constants

	// MainActivity.class
	static String myurl = "http://103.5.112.91/2c3fa05a103d78ccf08c4df3c00dedda.php";
	static String query1 = "apikey";

	// R.class
	public static final int mykey = 2131427360;

	// ./values/strings.xml
    <string name="mykey">h4ck3r801</string>

### Analysis

From this, we can see the url is `http://103.5.112.91/2c3fa05a103d78ccf08c4df3c00dedda.php`

And we append the param `apikey` with the MD5 of `h4ck3r801`

Run some simple code to get the MD5
	
	import java.security.MessageDigest;
	import java.security.NoSuchAlgorithmException;
	public class MyClass {

	    public static void main(String args[]) {
	            System.out.println(md5());
	    }
	        
	    public static final String md5() {
	        String str = "h4ck3r801";
	        try {
	          MessageDigest digest = MessageDigest.getInstance("MD5");
	          digest.update(str.getBytes());
	          
	          byte[] hash = digest.digest();

	          StringBuilder localStringBuilder = new StringBuilder();
	          int j = hash.length;
	          int i = 0;
	          while (i < j){
	            for (str = Integer.toHexString(hash[i] & 0xFF); str.length() < 2; str = "0" + str) {}
	            localStringBuilder.append(str);
	            i += 1;
	          }
	          str = localStringBuilder.toString();
	          return str;
	        } catch (NoSuchAlgorithmException localNoSuchAlgorithmException) {
	          localNoSuchAlgorithmException.printStackTrace();
	        }
	        return "";
	      }
	}


And we get

	10e37344984c8739801fee0eb1c46b3e

Finally, construct the URL

	$ curl http://103.5.112.91/2c3fa05a103d78ccf08c4df3c00dedda.php?apikey=10e37344984c8739801fee0eb1c46b3e
	Congrats!!Flag is xiomara{4ndr01d_15_1n_my_dn4} 

## Flag
`xiomara{4ndr01d_15_1n_my_dn4}`