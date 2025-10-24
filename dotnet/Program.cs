using System;
using System.Linq;
using Azure.AI.ContentSafety;
using Microsoft.Extensions.Configuration;
using Azure.Identity;

namespace Azure.AI.ContentSafety.Dotnet.Sample
{
    class ContentSafetySampleAnalyzeText
    {
        public static void AnalyzeText()
        {
            var configuration = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
                .Build();

            string? endpoint = configuration["AzureContentSafety:Endpoint"] ?? Environment.GetEnvironmentVariable("CONTENT_SAFETY_ENDPOINT");
            string? key = configuration["AzureContentSafety:Key"] ?? Environment.GetEnvironmentVariable("CONTENT_SAFETY_KEY");
            ContentSafetyClient client = new ContentSafetyClient(new Uri(endpoint), new AzureKeyCredential(key));

            // Example: analyze text without blocklist
            Console.WriteLine("Type your text:");

            string text = Console.ReadLine();

            var request = new AnalyzeTextOptions(text);

            Response<AnalyzeTextResult> response;
            try
            {
                response = client.AnalyzeText(request);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Analyze text failed: {0}", ex.Message);
                throw;
            }

            Console.WriteLine("\nAnalyze text succeeded:");
            Console.WriteLine("Hate severity: {0}", response.Value.CategoriesAnalysis.FirstOrDefault(c => c.Category == TextCategory.Hate)?.Severity ?? 0);
            Console.WriteLine("SelfHarm severity: {0}", response.Value.CategoriesAnalysis.FirstOrDefault(c => c.Category == TextCategory.SelfHarm)?.Severity ?? 0);
            Console.WriteLine("Sexual severity: {0}", response.Value.CategoriesAnalysis.FirstOrDefault(c => c.Category == TextCategory.Sexual)?.Severity ?? 0);
            Console.WriteLine("Violence severity: {0}", response.Value.CategoriesAnalysis.FirstOrDefault(c => c.Category == TextCategory.Violence)?.Severity ?? 0);
        }

        static void Main()
        {
            AnalyzeText();
        }
    }
}