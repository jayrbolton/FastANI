
package us.kbase.fastani;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: FastANIParams</p>
 * <pre>
 * fast_ani input
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "assembly_refs"
})
public class FastANIParams {

    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("assembly_refs")
    private List<String> assemblyRefs;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("workspace_name")
    public java.lang.String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public FastANIParams withWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("assembly_refs")
    public List<String> getAssemblyRefs() {
        return assemblyRefs;
    }

    @JsonProperty("assembly_refs")
    public void setAssemblyRefs(List<String> assemblyRefs) {
        this.assemblyRefs = assemblyRefs;
    }

    public FastANIParams withAssemblyRefs(List<String> assemblyRefs) {
        this.assemblyRefs = assemblyRefs;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((("FastANIParams"+" [workspaceName=")+ workspaceName)+", assemblyRefs=")+ assemblyRefs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
