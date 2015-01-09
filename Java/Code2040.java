import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject; 

/*
 * Code2040: This class will contain code for the 4 stages of the CODE2040 Challenges.
 *
 *author: Kelsey Jones
 *
 */
public class Code2040 
{

	public static void main(String[] args) 
	{
			
		
		JSONObject regDic = new JSONObject();
		regDic.put("email","kelsey.jones003@gmail.com");
		regDic.put("github","https://github.com/jones3kd/CODE2040-Challanges");

		//regDic = regDic.toString();
		String jsonRegDic = regDic.toString();
		String regUrl = "http://challenge.code2040.org/api/register";
		
		HttpClient client = HttpClientBuilder.create().build();
		
		try {
		HttpPost post = new HttpPost(regUrl);
		StringEntity params =new StringEntity(jsonRegDic);
		post.setEntity(params);
		HttpResponse response = client.execute(post);
		
		HttpEntity respEntity = response.getEntity();
		System.out.println(response.getStatusLine() + "\nmessage: " + respEntity.getContentType());
		
		if (respEntity != null)
		{
			String data = EntityUtils.toString(respEntity);
			JSONObject result = new JSONObject(data);
			
			System.out.println("response: "+ data);
		}
			
			
		}
		catch (Exception ex) {
	        System.err.print("register went wrong");
	    } finally {
	        client.getConnectionManager().shutdown();
	    }
	}

}
